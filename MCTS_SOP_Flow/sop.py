# sop.py
from models import generate_text
from prompt import generate_sop_prompt_from_task, generate_sop_prompt_from_step  # 导入新的提示词函数

class SOPGenerator:
    def __init__(self, model="gpt-4"):
        self.steps = []  # 用于存储已生成的SOP步骤
        self.model = model  # 选择使用的模型，默认 gpt-4

    def generate_sop(self, task_description):
        """生成SOP的步骤"""
        if not self.steps:  # 第一步
            prompt = generate_sop_prompt_from_task(task_description)
        else:  # 后续步骤
            prompt = generate_sop_prompt_from_step(self.steps[-1])

        # 使用模型生成SOP步骤
        sop_text = generate_text(prompt, model=self.model)
        
        # 避免重复步骤
        while sop_text in self.steps:
            sop_text = generate_text(generate_sop_prompt_from_task(task_description), model=self.model)  # 如果生成的步骤重复，再生成一次
        
        self.steps.append(sop_text.strip())  # 保存已生成的步骤，防止重复
        return sop_text.strip()  # 返回一个步骤，去除空白行
