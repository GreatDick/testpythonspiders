import requests
from bs4 import BeautifulSoup
import urllib
s=requests.Session()
data = {
    'username': 'guest',
    'password': 'guest',
}
def download(url, s):
    import urllib, os
    file_name = urllib.parse.unquote(url)
    file_name = file_name[file_name.rfind('/') + 1:]
    try:
        r = s.get(url, stream=True, timeout = 2)
        chunk_size = 1000
        timer = 0
        length = int(r.headers['Content-Length'])
        print('downloading {}'.format(file_name))
        if os.path.isfile('./' + file_name):
                    print('  file already exist, skipped')
                    return
        with open('./' + file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size):
                timer += chunk_size
                percent = round(timer/length, 4) * 100
                print('\r {:4f}'.format((percent)), end = '')
                f.write(chunk)
        print('\r  finished    ')
    except requests.exceptions.ReadTimeout:
        print('read time out, this file failed to download')
        return
    except requests.exceptions.ConnectionError:
        print('ConnectionError, this file failed to download')
        return
r=s.post('http://moodle.tipdm.com/login/index.php',data)
#print(r.url)
r = s.get('http://moodle.tipdm.com/course/view.php?id=16')
soup=BeautifulSoup(r.text,'lxml')
divs=soup.find_all('div',class_='activityinstance')
for div in divs[1:]: 
    url = div.a.get('href')
    r = s.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    target_div = soup.find('div', class_='resourceworkaround')
    target_url = target_div.a.get('href')
 #print(target_url)
    urllib.request.urlretrieve('http://moodle.tipdm.com/pluginfile.php/1583/mod_resource/content/1/5.3%20%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84.mp4','1.mp4')
            
input()