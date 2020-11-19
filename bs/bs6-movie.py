import requests
from bs4 import BeautifulSoup
#영화제목 점수 예매율, 상영시간을 추출하여 data\\movie.csv 저장
#영화포스터는 img폴더에 저장

url='https://movie.naver.com/movie/running/current.nhn'
recevd=requests.get(url)
dom=(recevd.text,'lxml')
title=dom.find('dt',class_='tit').find('a').text
print(title)