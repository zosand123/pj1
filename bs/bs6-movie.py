import requests
from bs4 import BeautifulSoup
#영화제목 점수 예매율, 상영시간을 추출하여 data\\movie.csv 저장
#영화포스터는 img폴더에 저장

def saveImg(imgUrl,title):
    fileName='../img/'+title+'.jpg'
    r=requests.get(imgUrl)
    with open(fileName,'wb') as f1:
        f1.write(r.content)

with open('..\\data\\movie.csv','w',encoding='utf-8') as f:
   url = 'https://movie.naver.com/movie/running/current.nhn#'
   recvd=requests.get(url)
   dom=BeautifulSoup(recvd.text,'lxml')
   tit=dom.find_all(class_='tit')
   div=dom.find_all(class_='thumb')
   for i in range(len(tit)):
       title=tit[i].find('a').text
       f.write(title+'\n')


