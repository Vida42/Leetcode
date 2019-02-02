# _*_ coding:utf-8 _*_ 
# 爬CSDN一些作者文章题目和链接

import urllib 
from bs4 import BeautifulSoup
from time import sleep
import random
import socket

def randHeader():
    
    head_connection = ['Keep-Alive']
    head_user_agent = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1', 
        'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10', 
        'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13', 
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+', 
        'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0', 
        'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124', 
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)']
    
    
    header = {
        'Connection': head_connection[0],
        'User-Agent': head_user_agent[random.randrange(0,len(head_user_agent))]
    }
    return header


def crawl():

    headers = randHeader()
    urls = ' '
    genre = '0'
    # tail = '?t=1&'
    genre_List = []
    for song in range(20,35):
        urln = urls +  str(song)

        try:
            request=urllib.request.Request(urln,headers = headers)
            page = urllib.request.urlopen(request,timeout = 5)
            contents = page.read()
            soup = BeautifulSoup(contents,'lxml')
            print(urln)

            # 如果有文章
            if not not soup.find('div', class_='article-item-box csdn-tracking-statistics'):
                # 获取文章名和链接
                for tag in soup.find_all('div', class_='article-item-box csdn-tracking-statistics'): 
                    locate_name = tag.find('h4')
                    # print(locate_name)
                    ixiami = locate_name.get_text()
                    # print(ixiami)
                    if '原' in ixiami:
                        print(True)
                        ixiami_name = ixiami.split('原')[1].strip()
                        # print(ixiami_name)
                        if locate_name.find('a', target = '_blank'):
                            # print(True)
                            locate_url = locate_name.find('a', target = '_blank')
                            # print(locate_url,'locate_url')
                            genre = locate_url['href']
                            genre_List.append(genre)

                        with open('result.txt', 'a', encoding="UTF-8") as f:
                            f.write(ixiami_name + '\t' + genre + '\n')
            # 否则另存
            else:
                with open('left.txt', 'a', encoding="UTF-8") as f:
                    f.write(urln + '\n')

        #该链接被删，报错，另存
        except urllib.error.HTTPError as e:
            print(e)

        # 超时，报错，另存
        except socket.timeout as e:
            print(e)

        # 设置爬取间隔
        sleep(random.uniform(1.7,2.0))


if __name__ == '__main__':
    crawl()