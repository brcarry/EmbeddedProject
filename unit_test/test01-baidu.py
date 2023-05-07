from aip import AipSpeech

# 替换为您的百度 API 密钥
BAIDU_APP_ID = 'xxx'
BAIDU_API_KEY = 'xxx'
BAIDU_SECRET_KEY = 'xxx'

# 创建一个 AipSpeech 对象
client = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)


def recognize_wav_file(filename):
    with open(filename, 'rb') as file:
        audio_data = file.read()

    response = client.asr(audio_data, 'wav', 16000, {'dev_pid': 1537})

    if response['err_no'] == 0:
        text = response['result'][0]
        return text
    else:
        print(f"识别错误：{response['err_no']} - {response['err_msg']}")
        return None


# 替换为您保存的 WAV 文件路径
wav_file_path = "output.wav"

recognized_text = recognize_wav_file(wav_file_path)

if recognized_text:
    print(f"识别结果：{recognized_text}")
else:
    print("识别失败")
