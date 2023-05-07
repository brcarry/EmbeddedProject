import openai
import os

# 设置 OpenAI API 密钥
openai.api_key = 'sk-xxx'

# 设置用于提示的文本
prompt = "你好呀"


def generate_reply(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60,
        n=1,
        temperature=0.5,
    )
    # print(response)
    return response.choices[0].message.content.strip()


# 打印生成的回复
print("start")
print(generate_reply(prompt))