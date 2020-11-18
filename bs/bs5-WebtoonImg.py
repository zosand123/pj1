import requests
from bs4 import BeautifulSoup
#bs4 패키지명을 피하기위해 bs5로 지정
#이미지까지 저장하기
def saveImg(imgUrl,title):
    # print(imgUrl)
    # print(imgUrl[-4:])
    # print(title)
    title=title.replace('.','') #.없애기
    filename='img\\'+title+imgUrl[-4:]
    # print(filename)
    r=requests.get(imgUrl)
    with open(filename,'wb') as f1:
        f1.write(r.content)

import time
with open('data/webtoon.csv','w',encoding='utf-8') as f:
    for page in range(1,5):
        pageurl='https://comic.naver.com/webtoon/list.nhn?titleId=739350&weekday=fri&page={}'.format(page)
        recvd=requests.get(pageurl)
        dom=BeautifulSoup(recvd.text,'lxml')
        table=dom.find('table',class_="viewList")

        # tbkid=table.children
        # for i in tbkid :
        #     print(i)
        #     print('-'*30)
        trs=table.find_all('tr')
        for i in range(2,len(trs)):
            # print(trs[i])
            img=trs[i].find('img')['src'] #이미지소스가져오기
            saveImg(img, title)

            td1=trs[i].find('td',class_='title')
            title=td1.find('a').text #제목
            div=trs[i].find('div',class_='rating_type')
            rate=div.find('strong').text #별점
            # print(rate)
            date=trs[i].find('td',class_='num').text #날짜
            # print(date)
            f.write('{},{},{}\n'.format(title, rate, date))
        time.sleep(1)
#모든페이지의 이미지를 다운로드 하고 제목,평점,등록일을 webtoon.csv파일로 저장
#단 한페이지 수집후 1초 쉬기