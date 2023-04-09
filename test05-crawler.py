import requests
from bs4 import BeautifulSoup


url = 'https://www.miyoushe.com/ys/home/28'
response = requests.get(url)
html = response.text

# 解析 HTML 内容
soup = BeautifulSoup(html, 'html.parser')

# print(html)

print(soup)