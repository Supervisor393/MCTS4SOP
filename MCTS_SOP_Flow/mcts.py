# mcts.py
import numpy as np
from sop import SOPGenerator
from agent import MultiAgentSystem  # 引入多智能体系统
from models import generate_text  # 引入模型生成文本的函数

# 定义节点类
class Node:
    def __init__(self, state, parent=None, depth=0):
        self.state = state  # 当前节点的状态，表示一个SOP步骤
        self.parent = parent  # 父节点
        self.children = []  # 子节点
        self.visits = 0  # 访问次数
        self.value = 0  # 节点的评估值
        self.reward = 0  # 节点的奖励值
        self.confidence = 0  # 大模型的置信度
        self.depth = depth  # 节点的深度

    def uct(self, parent_visits, c=1.41):
        """计算UCT值"""
        if self.visits == 0:
            return float('inf')
        return self.value / self.visits + c * np.sqrt(np.log(parent_visits) / self.visits)

class MCTS:
    def __init__(self, root_state, max_depth=10, model="gpt-4", debate_model="gpt-4"):
        self.root = Node(state=root_state)  # 根节点代表SOP的开始
        self.max_depth = max_depth  # 最大搜索深度
        self.sop_generator = SOPGenerator(model=model)  # 初始化 SOP 生成器，传入选择的模型
        self.multi_agent_system = MultiAgentSystem(debate_model=debate_model)  # 初始化多智能体系统并传递辩论模型

    def selection(self, node):
        """选择最优节点"""
        print(f"Selection phase: At node {node.state}")
        while node.children:
            node = max(node.children, key=lambda child: child.uct(node.visits))
            print(f"Selected child node {node.state} with UCT value {node.uct(node.visits)}")
        return node

    def expansion(self, node):
        """扩展节点"""
        print(f"Expansion phase: Expanding node {node.state}")
        if node.depth < self.max_depth:  # 控制扩展深度，超过最大深度不再扩展
            if len(node.children) < 3:  # 每个节点最多扩展3个子节点
                new_step = self.sop_generator.generate_sop(node.state)  # 根据当前步骤生成新的步骤
                if new_step:  # 确保生成的步骤不为空
                    new_node = Node(state=new_step, parent=node, depth=node.depth + 1)
                    node.children.append(new_node)
                    print(f"Expanded to new child node {new_node.state}")

    def simulation(self, node):
        """模拟：根据当前节点的状态进行模拟"""
        print(f"Simulation phase: Simulating from node {node.state}")
        
        # 收集从根节点到当前节点的SOP步骤路径
        path = []
        current_node = node
        while current_node:
            path.append(current_node.state)
            current_node = current_node.parent
        path.reverse()  # 反转路径，确保顺序从根节点到叶节点

        # 将整个路径传递给多智能体系统进行辩论和评估
        reward = self.multi_agent_system.evaluate_path(path)
        
        print(f"Simulation result (via multi-agent evaluation): {reward}")
        return reward

    def backpropagation(self, node, reward):
        """回溯：更新路径上的每个节点的评估值"""
        print(f"Backpropagation phase: Backpropagating reward {reward}")
        while node:
            node.visits += 1
            node.value += reward
            print(f"Updated node {node.state}: visits={node.visits}, value={node.value}")
            node = node.parent

    def search(self, iterations=5):
        """MCTS搜索"""
        print(f"Starting MCTS search with {iterations} iterations...")
        for i in range(iterations):
            print(f"\nIteration {i + 1}/{iterations}")
            node = self.selection(self.root)
            self.expansion(node)
            reward = self.simulation(node)
            self.backpropagation(node, reward)

        print("MCTS search completed.")

        # 获取优化后的SOP步骤
        sop_steps = []
        current_node = self.root
        # 将根节点到叶节点的路径收集为SOP步骤
        while current_node:
            sop_steps.append(current_node.state)
            if current_node.children:
                # 选择UCT值最优的子节点
                current_node = max(current_node.children, key=lambda child: child.uct(current_node.visits))
            else:
                break

        # 返回步骤列表（从根节点到叶节点的SOP步骤链）
        return sop_steps[::-1]  # 返回的是从根节点到叶节点的步骤链
