import requests
from bs4 import BeautifulSoup
url='https://movie.naver.com/movie/running/current.nhn'
recvd=requests.get(url)
dom=BeautifulSoup(recvd.text,'lxml')
tit=dom.find_all('dt',class_='tit')
rate=dom.find_all('span',class_='num')
with open('../data/movies.csv','w',encoding='utf-8') as f:
    for t in tit:
        title = t.find('a').text
    for r in rate:
        ra = r.text
        print(ra)