import requests
from bs4 import BeautifulSoup
br='--------'
with open('data.txt','wb') as f:
      headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
      r=requests.get('https://dianying.taobao.com',headers=headers)
      r.encoding = 'utf-8'
      content=r.text
      soup=BeautifulSoup(content,'lxml')
      dys=soup.find_all(class_='movie-card-list')
      dynames=soup.find_all(class_='movie-card-name')
      d=zip(dys,dynames)
      d=dict(d)
      print('正在热映的电影。。。')
      for dy,dyname in d.items():
         dyry=dy.get_text()
         dyn=dyname.get_text()
         print(dyn+dyry+'\n'+br)
         f.write(('正在热映的电影。。。'+'\n'+dyn+dyry+'\n'+br).encode('UTF-8'))
input()