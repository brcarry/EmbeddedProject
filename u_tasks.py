import jieba
import jieba.posseg as pseg
import requests
from urllib.parse import urlencode
import requests
import urllib
import json

def is_query_weather(text):
    # if(text=="查询天气")
    # return True
    if text == "查询天气":
        return True

    # 定义关键词列表
    keywords = ['天气', '气温', '温度']
    words = jieba.lcut(text)
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

    # message = str(input("要查询的城市："))


    url = "https://api.iyk0.com/tq/?city={}".format(city)  # 获取用户输入的城市进行查询
    request = url
    re = requests.get(request)
    rep = re.json()
    '''
    获取网页中的响应的元组变量
    '''
    code = rep.get('code')
    msg = rep.get('msg')
    city = rep.get('city')
    up = rep.get('update_time')
    wea = rep.get('wea')
    wea_img = rep.get('wea_img')
    tem = rep.get('tem')
    tem_day = rep.get('tem_day')
    tem_night = rep.get('tem_night')
    win = rep.get('win')
    win_speed = rep.get('win_speed')
    win_meter = rep.get('win_meter')
    air = rep.get('air')
    time = rep.get('time')

def is_query_music(text):
    return True

def query_music():
    pass


if __name__ == "__main__":
    print("[test]")
    # query_weather("test")

    params = {
        # "key": "你的API密钥",
        "key": "Sbx2dSeivSa3nS186",
        "location": "ip",  # 查询地点设置为访问IP所在地
        "language": "zh-Hans",
        "unit": "c",
    }

    url = "https://api.seniverse.com/v3/weather/now.json"

    # 获取数据
    r = requests.get(url, params=params)
    print(r)

    # 解析数据
    # data = r.json()["results"]
    data = r.json()


    print(data)