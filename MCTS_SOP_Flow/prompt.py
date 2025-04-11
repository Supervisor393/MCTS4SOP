# prompt.py

# 针对任务描述生成SOP的第一步的提示词
def generate_sop_prompt_from_task(task_description):
    return f"""
    Generate a clear, concise, and unique step in the Standard Operating Procedure (SOP) for the task described below.
    Your answer only contain the content of the step, not appear of "step 1".  
    The first step should provide a high-level overview or a general instruction that sets the stage for the task. 
    It should focus on the main objective and what needs to be accomplished in the overall task.

    Task: {task_description}
    """

# 针对已有步骤生成SOP后续步骤的提示词
def generate_sop_prompt_from_step(previous_step):
    return f"""
    Based on the following SOP step, generate the next step in the Standard Operating Procedure (SOP). 
    The next step should provide more specific, actionable details that build upon the previous step.
    The new step should be unique and focus on an important part of the task that hasn’t been fully addressed yet.
     Your answer only contain the content of the step, not appear the "next step". 
    Previous step: {previous_step}
    """
