import requests
from bs4 import BeautifulSoup
import urllib
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
print('一言(10条)')
def yiyan():
           r=requests.get('http://hitokoto.cn',headers=headers)
            # r.encoding='UTF-8'
           content=r.text
           soup=BeautifulSoup(content,'lxml')
            #print(soup)
           au=soup.find('p',class_='text_author')
           ss=soup.select('p.text')
           hito=ss[0].text
           ko=ss[1].text
           to=ss[2].text
           print(hito+ko+to+au.get_text()+'\n')
#n=input('获取的条数:')
#t=int(n)
for i in range(1,10):
	yiyan()