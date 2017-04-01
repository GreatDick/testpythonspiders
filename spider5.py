import requests
from bs4 import BeautifulSoup
s=requests.Session()
data = {
    'username': 'guest',
    'password': 'guest',
}
r=s.post('http://moodle.tipdm.com/login/index.php',data)
#print(r.url)
r = s.get('http://moodle.tipdm.com/course/view.php?id=16')
soup=BeautifulSoup(r.text,'lxml')
divs=soup.find_all('div',class_='activityinstance')
for div in divs[1:]:  # 注意这里也出现了改动
    url = div.a.get('href')
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    target_div = soup.find('div', class_='resourceworkaround')
    target_url = target_div.a.get('href')
    print(target_url)
input()