from hotword import snowboydecoder
import sys
import signal
import speech_recognition as sr
from aip import AipSpeech
import openai

import u_record

# 替换为您的百度 API 密钥
BAIDU_APP_ID = '32155615'
BAIDU_API_KEY = 'nX0LOylXs4kpEbdu5y4qkraC'
BAIDU_SECRET_KEY = 'ARhpetgVDPbu2QCWI41AHaRzRjsY9lKi'

# 替换为您的 OpenAI API 密钥
# OPENAI_API_KEY = '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'
OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY

# 创建一个 AipSpeech 对象
baidu_client = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)

interrupted = False

# 将用户的语音保存为文件
def save_audio_to_file(audio, filename):
    with open(filename, "wb") as file:
        file.write(audio.get_wav_data())

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def detected_callback():
    print("唤醒词已检测到！")
    recognize_and_respond()

def recognize_and_respond():

    print("正在倾听您的问题...")
    u_record.record_wav("output.wav")
    # try:
    print("正在识别语音...")
    # 将音频转换为可识别的格式
    # audio_data = audio.get_wav_data()
    audio_data = open("output.wav","rb").read()
    # 1537表示中文
    response = baidu_client.asr(audio_data, 'wav', 16000, {'dev_pid': 1537})

    # print(response)
    if response['err_no'] == 0:
        text = response['result'][0]
        print(f"您说了：{text}")

        response_text = generate_response(text)
        print(f"助手回答：{response_text}")

    else:
        print("抱歉，我没有听清楚。")


def generate_response(prompt):
    print("开始生成回复...")
    # response = openai.Completion.create(engine="davinci-codex", prompt=prompt, max_tokens=50, n=1, stop=None, temperature=0.5)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # print(response)

    message = response.choices[0].text.strip()
    return message

# 替换为您的模型文件路径
model_path = './hotword/resources/models/paimeng.pmdl'

signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model_path, sensitivity=0.5)
print("正在监听唤醒词，请说话...")

# main loop
detector.start(detected_callback=detected_callback,
              interrupt_check=interrupt_callback,
              sleep_time=0.03)

detector.terminate()
