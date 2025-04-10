import argparse
from sop import SOPGenerator
from mcts import MCTS

def run():
    task_description = "Diagnose the root cause of a system failure"
    sop_generator = SOPGenerator()
    mcts = MCTS(root_state=task_description, max_depth=5)

    # 逐步生成SOP步骤并扩展每个步骤
    sop_steps = []
    root_node = mcts.root
    current_state = root_node.state

    # 首先，生成第一个步骤
    first_step = sop_generator.generate_sop(current_state)
    sop_steps.append(first_step)
    
    # 使用MCTS逐步生成每个SOP步骤
    for i in range(1, mcts.max_depth):  
        current_state = sop_steps[-1]  # 当前的步骤
        print(f"Current step: {current_state}")
        
        # 在每次迭代时，根据当前的步骤生成新的步骤
        next_step = sop_generator.generate_sop(current_state)
        sop_steps.append(next_step)
    
    print("Generated SOP steps:")
    for step in sop_steps:
        print(step)

    # 使用MCTS优化生成的SOP步骤
    sop_steps = mcts.search(iterations=5)
    print("Optimized SOP using MCTS:")
    for step in sop_steps:
        print(step)

if __name__ == "__main__":
    run()
