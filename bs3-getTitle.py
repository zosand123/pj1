#www.naver.com/robots.txt 사이트 정책보기! disallow면 비허용
import requests
from bs4 import BeautifulSoup
# url='https://finance.naver.com/marketindex/'
# recvd=requests.get(url)
# print(recvd)
# print(recvd.text)
# dom=BeautifulSoup(recvd.text,'lxml')
# span=dom.find('span',class_="value")
# print(span.text)
#<span class="value">1,107.00</span>

#tbody는 웹에서 만들어주는 경우가 많아 원본소스에 없을 수 있음
#csv : comma-separated values
# with open('data/webtoon.csv','w',encoding='utf-8') as f:
#     url='https://comic.naver.com/webtoon/list.nhn?titleId=739350&weekday=fri&page=1'
#     recvd=requests.get(url)
#     dom=BeautifulSoup(recvd.text,'lxml')
#     table=dom.find('table',class_="viewList")
#
#     # tbkid=table.children
#     # for i in tbkid :
#     #     print(i)
#     #     print('-'*30)
#     trs=table.find_all('tr')
#     for i in range(2,len(trs)):
#         # print(trs[i])
#         td1=trs[i].find('td',class_='title')
#         title=td1.find('a').text
#         # print(title)
#         div=trs[i].find('div',class_='rating_type')
#         rate=div.find('strong').text
#         # print(rate)
#         date=trs[i].find('td',class_='num').text
#         # print(date)
#         f.write('{},{},{}\n'.format(title, rate, date))

# for page in range(1,5):
#     str='https://comic.naver.com/webtoon/list.nhn?titleId=739350&weekday=fri&page={}'.format(page)
#     print(str)

#이미지경로,제목,평점,등록일 추출
import time #컴퓨터쉬게하기
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
            td1=trs[i].find('td',class_='title')
            title=td1.find('a').text #제목
            # print(title)
            div=trs[i].find('div',class_='rating_type')
            rate=div.find('strong').text
            # print(rate)
            date=trs[i].find('td',class_='num').text
            # print(date)
            f.write('{},{},{},{}\n'.format(img, title, rate, date))
        #time.sleep(1) #한페이지하고 1초 쉬게하기
#--------------------------------------------------------------------------------

