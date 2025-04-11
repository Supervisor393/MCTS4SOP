# agent.py
import random
from models import generate_text  # 引入生成文本的模型

class DebateAgent:
    def __init__(self, name, role, model="gpt-4"):
        self.name = name
        self.role = role  # 角色区分：领域专家、步骤连贯性专家、预测专家
        self.model = model  # 传入模型参数

    def debate(self, path, model="gpt-4"):
        """进行辩论，给出对整条路径的评估"""
        # 将路径中的所有步骤合并为一个大的字符串
        path_text = " -> ".join(path)  # 每个步骤用" -> "连接起来
        prompt = self.generate_prompt(path_text)
        score = self.evaluate_step(prompt, model)
        return score

    def generate_prompt(self, path_text):
        """根据智能体角色生成不同的提示词"""
        if self.role == "domain_expert":
            return f"Evaluate the technical correctness and relevance of the following SOP steps: {path_text}. Provide only a score from 0 to 1, with 1 being highly effective, based on the depth and accuracy of the actions described. Remember only a number."
        elif self.role == "coherence_expert":
            return f"Assess the coherence and logical flow of the following SOP steps: {path_text}. Does it logically fit into the overall task sequence? Provide only a score from 0 to 1, with 1 being highly effective. Remember only a number."
        elif self.role == "predictor":
            return f"Based on the following SOP steps, predict how likely these steps will help in successfully identifying the root cause of the system failure. Provide a score from 0 to 1, with 1 being highly effective. Remember only a number."
        else:
            return f"Evaluate the following SOP steps: {path_text}"

    def evaluate_step(self, prompt, model="gpt-4"):
        """使用模型对整条路径进行评估"""
        response = generate_text(prompt, model=model, max_tokens=1500)  # 增加最大token数，以便完整处理路径
        # 这里根据模型返回的结果进行解析并转换为一个评分（0到1之间）
        try:
            score = float(response)
        except ValueError:
            score = random.uniform(0, 1)  # 如果模型返回非数字，则使用随机评分
        return score


class MultiAgentSystem:
    def __init__(self, debate_model="gpt-4"):
        self.agents = [
            DebateAgent(f"Agent_{i}", role, model=debate_model) for i, role in enumerate(["domain_expert", "coherence_expert", "predictor"])
        ]  # 三个不同角色的智能体，并传递模型给每个智能体

    def evaluate_path(self, path, model="gpt-4"):
        """让所有智能体对整条路径进行评估"""
        agent_scores = [self.evaluate_step(path, model) for agent in self.agents]
        # 返回三个智能体的评分，进行加权计算
        weights = [0.4, 0.3, 0.3]  # 假设领域专家评分占40%，连贯性专家占30%，预测专家占30%
        
        # 每个路径的分数计算
        weighted_score = sum(agent_scores[i] * weights[i] for i in range(len(agent_scores)))
        return weighted_score

    def evaluate_step(self, path, model="gpt-4"):
        """对整条路径进行辩论，获取评分"""
        agent_scores = [agent.debate(path, model) for agent in self.agents]
        # 按权重加权计算最终评分（可根据实际需求调整权重）
        weights = [0.4, 0.3, 0.3]  # 假设领域专家评分占40%，连贯性专家占30%，预测专家占30%
        weighted_score = sum(score * weight for score, weight in zip(agent_scores, weights))
        return weighted_score
