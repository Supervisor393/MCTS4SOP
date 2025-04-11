# main.py
from sop import SOPGenerator
from mcts import MCTS

def run():
    task_description = "Diagnose the root cause of a system failure"
    
    # 设置 MCTS 的最大深度和迭代次数
    max_depth = 3  # 最大深度
    iterations = 5  # 迭代次数

    # 选择生成SOP的模型，可以选择 gpt-3.5-turbo 或 gpt-4
    sop_model_choice = "gpt-4"  

    # 选择辩论模型，可以选择 gpt-3.5-turbo 或 gpt-4
    debate_model_choice = "gpt-4"  

    # 初始化 MCTS，传递任务描述、最大深度和模型选择
    mcts = MCTS(root_state=task_description, max_depth=max_depth, model=sop_model_choice, debate_model=debate_model_choice)

    # 使用 MCTS 控制 SOP 生成过程
    print(f"Starting MCTS to generate SOP for: {task_description}")
    sop_steps = mcts.search(iterations=iterations)

    # 输出生成的 SOP 步骤
    print("\nGenerated SOP steps:")
    print(sop_steps)

if __name__ == "__main__":
    run()
