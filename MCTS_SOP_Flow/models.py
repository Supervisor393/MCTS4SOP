# models.py
import openai

# 使用你自己的 OpenAI API 密钥
openai.api_key = 'sk-YCumRzgNNd5zmAH0Nc61OG7nfzy0sd2kfyBvsratmhQr6qhB'

# 假设你有一个不同的 API URL 地址
openai.api_base = "https://api.chatanywhere.tech"  # 替换为你要使用的 URL

# 使用 GPT-3.5 或 GPT-4 生成文本
def generate_text(prompt, model="gpt-3.5-turbo", max_tokens=1500):
    # 使用聊天模型的 v1/chat/completions 端点
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=1.0
    )
    return response['choices'][0]['message']['content'].strip()
