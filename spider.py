import requests
from bs4 import BeautifulSoup
br='----分割线----'
#with open('data.txt','wb') as f:
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get('http://www.qiushibaike.com', headers = headers)
content = r.text
soup = BeautifulSoup(r.text, 'lxml')
divs = soup.find_all(class_ = 'article block untagged mb15')
for div in divs:
    if div.find_all(class_ = 'thumb'):
        continue
    joke = div.span.get_text()
    print(joke)
    print('------')
input()
#f.write(joke.encode('UTF-8'))
# f.write(br.encode('UTF-8'))