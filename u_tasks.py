import jieba
import jieba.posseg as pseg
import requests
from urllib.parse import urlencode
import requests
import urllib
import json

from miyoubiAuto.ys import signInYS, getYSArticle
import miyoubiAuto
from miyoubiAuto import ys, Global

jieba.setLogLevel(jieba.logging.INFO)

def hztq():
    url = 'https://www.hzqx.com/hztq/data/actualNewestData/58457.json'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Content-type": "application/x-www-form-urlencoded",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Cookie": ""
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        content_json = response.json()
        # print(content_json)
        # print(content_json['forecast1'])

        text = content_json['forecast1']
        text = text.split("：", 1)
        text = text[1]
        text = text.replace('%', '')
        # print(text)
        return text
    else:
        return "杭州天气查询失败"



def is_query_weather(text):

    if text == "查询天气":
        return True

    # 定义关键词列表
    keywords = ['天气', '气温', '温度']
    words = jieba.lcut_for_search(text, HMM=True)
    # 检查是否包含关键词
    if any(word in keywords for word in words):
        return True
    else:
        return False

def query_weather(text):
    words = pseg.cut(text)
    city = "杭州"
    for word, flag in words:
        if flag == 'ns':  # ns 表示地名
            city = word
            break
    if city == "杭州":
        return hztq()

    params = {
        # "key": "你的API密钥",
        "key": "Sbx2dSeivSa3nS186",
        # "location": "ip",  # 查询地点设置为访问IP所在地
        "location": city,  # 查询地点设置为访问IP所在地
        "language": "zh-Hans",
        "unit": "c",
    }
    url = "https://api.seniverse.com/v3/weather/now.json"
    # 获取数据
    r = requests.get(url, params=params)
    # print(r)
    # 解析数据
    data = r.json()["results"]
    # print(data)

    ret = ""
    ret += data[0]["location"]["name"]
    ret += "的天气是"
    ret += data[0]["now"]["text"]

    print(ret)
    return ret


def is_query_music(text):
    return True

def query_music():
    pass


def getYSArticle():
    # print("111")
    ret =  ys.getYSArticle()
    # print(ret)
    return ret

def signYS():
    # print("222")
    ret = ys.signInYS()
    if ret:
        return "签到成功"
    else:
        return "请勿重复签到"


if __name__ == "__main__":
    print("[test]")

    text = "北京天气怎么样？"
    print(is_query_weather("北京天气怎么样？"))
    query_weather(text)