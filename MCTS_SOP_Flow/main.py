# main.py
from sop import SOPGenerator
from mcts import MCTS

def run():
    task_description = "Diagnose the root cause of a system failure"
    
    # 初始化MCTS，根节点为任务描述
    mcts = MCTS(root_state=task_description, max_depth=5, max_steps=5)

    # 使用MCTS控制SOP生成过程
    print(f"Starting MCTS to generate SOP for: {task_description}")
    sop_steps = mcts.search(iterations=5)

    # 输出生成的SOP步骤
    print("\nGenerated SOP steps:")
    formatted_sop = mcts.sop_generator.get_formatted_sop()  # 获取格式化的SOP步骤
    print(formatted_sop)

if __name__ == "__main__":
    run()
