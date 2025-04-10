import numpy as np
import random
from agent import MultiAgentSystem
from sop import SOPGenerator

class Node:
    def __init__(self, state, parent=None):
        self.state = state  # 当前节点的状态，表示一个SOP步骤
        self.parent = parent  # 父节点
        self.children = []  # 子节点
        self.visits = 0  # 访问次数
        self.value = 0  # 节点的评估值
        self.reward = 0  # 节点的奖励值

    def uct(self, parent_visits, c=1.41):
        """计算UCT值"""
        if self.visits == 0:
            return float('inf')
        return self.value / self.visits + c * np.sqrt(np.log(parent_visits) / self.visits)

class MCTS:
    def __init__(self, root_state, max_depth=10):
        self.root = Node(state=root_state)  # 根节点代表SOP的开始
        self.max_depth = max_depth
        self.multi_agent_system = MultiAgentSystem()  # 初始化多智能体系统
        self.sop_generator = SOPGenerator()  # 初始化SOP生成器

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
        # 每个节点扩展3个子节点，表示每个步骤的不同选项
        for i in range(3):  # 假设每个步骤有3个选项
            new_step = self.sop_generator.generate_sop(node.state)  # 根据当前步骤生成新的步骤
            new_node = Node(state=f"{node.state}_step_{i}: {new_step}", parent=node)
            node.children.append(new_node)
            print(f"Expanded to new child node {new_node.state}")

    def simulation(self, node):
        """模拟：根据当前节点的状态进行模拟"""
        print(f"Simulation phase: Simulating from node {node.state}")
        # 使用多智能体系统对节点进行评估，模拟结果作为奖励
        reward = self.multi_agent_system.evaluate_step(node.state)
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
        while current_node:
            sop_steps.append(current_node.state)
            current_node = current_node.parent

        # 返回步骤列表（从根节点到叶节点的SOP步骤链）
        return sop_steps[::-1]  # 返回的是从根节点到叶节点的步骤链

# 测试MCTS
if __name__ == "__main__":
    mcts = MCTS(root_state="Diagnose the root cause of a system failure", max_depth=5)
    sop_steps = mcts.search(iterations=5)
    print(f"\nOptimized SOP using MCTS:")
    for step in sop_steps:
        print(step)
