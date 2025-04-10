import openai

# 初始化OpenAI API
openai.api_key = ''

# 使用GPT-3.5聊天模型进行文本生成
def generate_text(prompt, model="gpt-3.5-turbo", max_tokens=100):
    # 使用聊天模型的 v1/chat/completions 端点
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=1.0
    )
    return response['choices'][0]['message']['content'].strip()

# 使用GPT-4聊天模型进行文本生成
def generate_text_gpt4(prompt, model="gpt-4", max_tokens=100):
    # 使用聊天模型的 v1/chat/completions 端点
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=1.0
    )
    return response['choices'][0]['message']['content'].strip()
