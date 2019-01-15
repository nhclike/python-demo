# coding:utf-8

import requests
import re

goods = '水杯'
url = 'https://s.taobao.com/search?q=' + goods

r = requests.get(url=url, timeout=10)
html = r.text

tlist = re.findall(r'\"raw_title\"\:\".*?\"', html)  # 正则提取商品名称
plist = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)  # 正则提示商品价格

print(tlist)
print(plist)
print(type(plist))  #  正则表达式提取出的商品名称和商品价格都是以列表形式存储数据的