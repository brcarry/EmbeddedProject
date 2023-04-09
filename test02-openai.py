import openai
import os

# 设置 OpenAI API 密钥
# openai.api_key = os.environ["OPENAI_API_KEY"]
# openai.api_key = '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'
openai.api_key = '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'

# 设置用于提示的文本
prompt = "你叫什么名字？"

# 使用 OpenAI API 生成对话回复
def generate_reply(prompt):
    response = openai.Completion.create(
        # engine="text-davinci-002",
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# 打印生成的回复

# openai.Model.list()
print(generate_reply(prompt))
