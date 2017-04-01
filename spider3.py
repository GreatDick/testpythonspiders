import requests
from bs4 import BeautifulSoup
headers ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r=requests.get('https://www.v2ex.com/?tab=tech',headers=headers)
r.encoding = 'utf-8'
content=r.text
soup=BeautifulSoup(content,'lxml')
xws=soup.find_all(class_='item_title')
for xw in xws:
   dayxw=xw.get_text() 
   print(dayxw)
   print('-------')
input()