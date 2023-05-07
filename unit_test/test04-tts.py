from aip import AipSpeech

# 百度语音合成 API 的参数
BAIDU_APP_ID = '32155615'
BAIDU_API_KEY = 'nX0LOylXs4kpEbdu5y4qkraC'
BAIDU_SECRET_KEY = 'ARhpetgVDPbu2QCWI41AHaRzRjsY9lKi'

baidu_client = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)

# 要转换为语音的文本内容
text = '你好，这是一个测试。'

# 调用语音合成 API 生成语音文件
result = baidu_client.synthesis(text, 'zh', 1, {
    'vol': 5,
    'per': 0,
})

# 将语音文件保存到本地
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
