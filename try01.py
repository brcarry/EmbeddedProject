# from hotword import snowboydecoder
from hotword import snowboydecoder
import sys
import signal
import speech_recognition as sr
import openai

# 替换为您的百度 API 密钥
BAIDU_APP_ID = '32155615'
BAIDU_API_KEY = 'nX0LOylXs4kpEbdu5y4qkraC'
BAIDU_SECRET_KEY = 'ARhpetgVDPbu2QCWI41AHaRzRjsY9lKi'

# 替换为您的 OpenAI API 密钥
OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY

interrupted = False


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
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("正在倾听您的问题...")
        audio = r.listen(source)

    try:
        print("正在识别语音...")
        text = r.recognize_baidu(audio, app_id=BAIDU_APP_ID, api_key=BAIDU_API_KEY, secret_key=BAIDU_SECRET_KEY,
                                 language='zh')
        print(f"您说了：{text}")

        response = generate_response(text)
        print(f"助手回答：{response}")

    except sr.UnknownValueError:
        print("抱歉，我没有听清楚。")
    except sr.RequestError as e:
        print(f"请求错误：{e}")


def generate_response(prompt):
    response = openai.Completion.create(engine="davinci-codex", prompt=prompt, max_tokens=50, n=1, stop=None,
                                        temperature=0.5)
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