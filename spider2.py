# -*- coding: utf-8 -*-
__author__ = 'duohappy'

import requests
import time
from bs4 import BeautifulSoup

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}

# 建立城市和网址特殊部分的对应关系
#weather_code = {'北京':'101010100','上海':'101020100','深圳':'101280601', '广州':'101280101', '杭州':'101210101'}

#city = input('请输入城市名：')  # 仅仅能输入北京，上海，广州，深圳，杭州

url = "http://www.weather.com.cn/weather1d/101190701.shtml"

web_data = requests.get(url, headers=headers)
web_data.encoding = 'utf-8'

content = web_data.text

soup = BeautifulSoup(content, 'lxml')

tag_list = soup.select('p.tem span')
tq=soup.select('p.wea')
#zl =soup.select('div.zs.pol span a')
day_temp = tag_list[0].text
night_temp = tag_list[1].text
#kqzl =zl[0].text
tqqk1=tq[0].text
tqqk2=tq[1].text
print(time.strftime("%Y:%m:%d"))
print('盐城今日天气'+'\n'+'白天温度为{0}℃\n晚上温度为{1}℃'.format(day_temp,night_temp)+'\n'+'白天天气情况:{0}\n夜间天气情况:{1}'.format(tqqk1,tqqk2))
print('(按回车退出)')
input()