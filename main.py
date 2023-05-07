from hotword import snowboydecoder
import sys
import signal
import speech_recognition as sr
from playsound import playsound
from aip import AipSpeech
import openai
import time
import u_record
import u_tasks
import socket
from playsound import playsound

server_addr = '10.181.243.251'
server_port = 6666

# 替换为您的百度 API 密钥
BAIDU_APP_ID = 'xxx'
BAIDU_API_KEY = 'xxx'
BAIDU_SECRET_KEY = 'xxx'

# 替换为您的 OpenAI API 密钥
OPENAI_API_KEY = 'sk-xxx'

MAX_LENGTH = 100


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
    playsound("paimon_response.mp3")
    time.sleep(1)
    # print("唤醒词已检测到！")
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

        response_text = ""
        # 判断是否为特殊任务
        if text == "一键签到。":
            response_text = u_tasks.signYS()
        elif text == "我要看帖子。":
            response_text = u_tasks.getYSArticle()
        elif u_tasks.is_query_weather(text):
            response_text = u_tasks.query_weather(text)
        else:
            # 若都不是，则调用chatgpt的api生成回复

            # add length limit
            text += "请用中文回答，并控制在{}字以内。".format(MAX_LENGTH)
            response_text = generate_response(text)

        # chatgpt 回复文字 -> 语音(调用百度api)
        # tts_result = baidu_client.synthesis(response_text, 'zh', 1, {'vol': 5,'per': 0,})
        # if not isinstance(tts_result, dict):
        #     with open('audio.mp3', 'wb') as f:
        #         f.write(tts_result)

        sk_pi = socket.socket()
        sk_pi.connect((server_addr, server_port))

        text = response_text
        sk_pi.send(text.encode('utf-8'))

        ret = sk_pi.recv(1024).decode('utf-8')
        len_file = int(ret)
        sk_pi.send("即将接收大小为{}的文件".format(len_file).encode('utf-8'))

        save_filename = 'audio.mp3'
        already_receive = 0
        with open(save_filename,'wb+') as f:
            while True:
                ret = sk_pi.recv(1024)
                f.write(ret)
                already_receive += len(ret)
                if already_receive >= len_file:
                    break

        print(f"助手回答：{response_text}")
        playsound('audio.mp3')

    else:
        print("抱歉，我没有听清楚。")


def generate_response(prompt):
    print("等待chatgpt生成回复...")
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
    
    message = response.choices[0].message.content.strip()
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