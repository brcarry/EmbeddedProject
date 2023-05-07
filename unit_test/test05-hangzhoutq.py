# 这个会403
# import requests
# from bs4 import BeautifulSoup
#
# # 发送请求获取页面内容
# url = 'https://www.hzqx.com/hztq/index.html'
# response = requests.get(url)
#
# # 检查请求是否成功
# if response.status_code == 200:
#     # 解析HTML
#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup)
#
# else:
#     print(f'请求失败，状态码：{response.status_code}')


import requests

url = 'https://www.hzqx.com/hztq/data/actualNewestData/58457.json'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Content-type":"application/x-www-form-urlencoded",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Cookie":""
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    content_json = response.json()
    print(content_json)
    print(content_json['forecast1'])

    text = content_json['forecast1']
    text = text.split("：", 1)
    text = text[1]
    text = text.replace('%','')
    print(text)
else:
    print(f'请求失败，状态码：{response.status_code}')
