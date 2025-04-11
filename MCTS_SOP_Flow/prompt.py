# prompt.py

# 针对任务描述生成SOP的第一步的提示词
def generate_sop_prompt_from_task(task_description):
    return f"""
    Generate a clear, concise, and unique step in the Standard Operating Procedure (SOP) for the task described below.
    Your answer should only contain the content of the step, not the phrase "step 1".
    The first step should provide a high-level overview or a general instruction that sets the stage for the task. 
    It should focus on the main objective and what needs to be accomplished in the overall task. Make sure the instruction is action-oriented, clear, and brief. Each step should describe **only one action** and avoid including multiple instructions or substeps in a single step.

    Example structure for SOP steps (for better clarity on the expected format):
    1. high_level_action: A clear, high-level action verb describing the task.
    2. next_step_action: A subsequent specific action that builds on the previous step.
    3. further_details: Any additional explanation, context, or instructions that support the execution of the previous steps.
    4. observation_or_conclusion: A short, actionable observation or result of the previous steps.
    
    Each action should be simple and concise, describing **only one thing to be done at a time**. For example, avoid combining two or more instructions in one step.

    Example SOP for 'Generate SOP for IO error':
    1. get_relevant_metric: Retrieve and review the relevant metrics related to the anomaly.
    2. whether_is_abnormal_metric: Check if the IO metrics are abnormal by comparing with thresholds.
    3. collect_trace: Gather trace data for the anomalous service to investigate further.
    4. observations: Document the observations from the collected metrics and traces to guide troubleshooting.

    Task: {task_description}
    """

# 针对已有步骤生成SOP后续步骤的提示词
def generate_sop_prompt_from_step(previous_step):
    return f"""
    Based on the following SOP step, generate the next step in the Standard Operating Procedure (SOP). 
    The next step should provide more specific, actionable details that build upon the previous step.
    The new step should be unique and focus on an important part of the task that hasn’t been fully addressed yet. 
    Your answer should only contain the content of the step, not the phrase "next step". Make sure that each step contains **only one action** to be performed. Avoid adding multiple instructions or substeps in a single step.

    Example structure for SOP steps (for better clarity on the expected format):
    1. high_level_action: A clear, high-level action verb describing the task.
    2. next_step_action: A subsequent specific action that builds on the previous step.
    3. further_details: Any additional explanation, context, or instructions that support the execution of the previous steps.
    4. observation_or_conclusion: A short, actionable observation or result of the previous steps.

    Example SOP for 'Generate SOP for IO error':
    1. get_relevant_metric: Retrieve and review the relevant metrics related to the anomaly.
    2. whether_is_abnormal_metric: Check if the IO metrics are abnormal by comparing with thresholds.
    3. collect_trace: Gather trace data for the anomalous service to investigate further.
    4. observations: Document the observations from the collected metrics and traces to guide troubleshooting.

    Previous step: {previous_step}
    """
