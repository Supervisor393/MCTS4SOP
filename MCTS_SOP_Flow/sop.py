from models import generate_text

class SOPGenerator:
    def __init__(self):
        self.steps = []

    def generate_sop(self, task_description):
        """生成SOP的步骤"""
        prompt = f"Please generate the next step in the Standard Operating Procedure (SOP) for the following task: {task_description}"
        sop_text = generate_text(prompt)
        return sop_text.strip()  # 返回一个步骤，去除空白行

    def evaluate_sop(self, sop_steps):
        """评估生成的SOP"""
        return sum([len(step) for step in sop_steps])  # 一个简单的评分方法，实际可以更复杂
