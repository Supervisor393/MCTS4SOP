import random

class DebateAgent:
    def __init__(self, name):
        self.name = name

    def debate(self, step):
        """进行辩论，给出对该步骤的评估"""
        return random.choice([1, -1])  # 随机给出评估

class MultiAgentSystem:
    def __init__(self):
        self.agents = [DebateAgent(f"Agent_{i}") for i in range(3)]  # 三个辩论智能体

    def evaluate_step(self, step):
        """让所有智能体对每个SOP步骤进行评估"""
        scores = [agent.debate(step) for agent in self.agents]
        return sum(scores) / len(scores)  # 返回平均评分
