import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import os
import cx_Oracle
# url='https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K'
#
# recvd=requests.get(url)
# #상세페이지의 차이름+가격+기본정보를 데이터베이스에 입력하고 (첫번째)이미지는 car폴더에저장
# dom=BeautifulSoup(recvd.text,'lxml')
# alist=dom.select('#listCont div.mode-cell.title > p.tit > a')
# baseurl='https://www.bobaedream.co.kr'
# urllist=[]
# for a in alist:
#     # print(baseurl+a['href'])
#     # print(urljoin(baseurl,a['href']))
#     urllist.append(urljoin(baseurl,a['href']))
# # print(urllist)
# for detailurl in urllist:
#     r=requests.get(detailurl)
#     d=BeautifulSoup(r.text,'lxml')
#     title=d.select_one('#bobaeConent div.title-area > h3.tit').text
#     price=d.select_one('#bobaeConent div.price-area > span > b').text+'만원'
#     # print(title,price)
#     imgs=d.select('#bx-pager img')
#     # print(imgs)
#     imglist=[]
#     for img in imgs:
#         # imglist.append
#         # print("https:"+img['src'])
#         if(img['src'][2:6]=='file'):
#             imglist.append('http:'+img['src'])
#     # print(imglist)
#     infos=d.select('#bobaeConent div.info-basic > div > table tr') #기본정보 tr를 통째로 가져온다
#     # print(len(infos))
#     # print(infos[0])
#     infolist=infos[0].text.strip().split('\n') #하나씩 쪼개서 분배
#     year=infolist[1]
#     baegi=infolist[3]
#     infolist = infos[1].text.strip().split('\n')
#     km=infolist[1]
#     color=infolist[3]
#     infolist = infos[2].text.strip().split('\n')
#     # print(infolist)
#     trans=infolist[1]
#     garantee=infolist[-1]
#     infolist = infos[3].text.strip().split('\n')
#     fuel = infolist[1]
#     confirm = infolist[-1]
#     if confirm=='확인사항': #확인사항끝에 정보없으면 확인사항이라고 떠서 공백으로처리
#         confirm=''
#     str="{},{},{},{},{},{},{},{},{},{}"
#     print(str.format(title,price,year,baegi,km,color,trans,garantee,fuel,confirm))
#------------------------------------------------------------------------------------


def saveImg(imglist,title):
    i=0
    for imgurl in imglist:
        i=i+1
        filename=os.path.join('d:\\','study','pj1','car',title.strip().replace(" ","")+str(i)+imgurl[-4:])
        # 실행파일만들때는 절대경로써줘야함
        #'d:\\' os.path.join을 쓰더라도 드라이버에는 \\붙여줘야한다.
        # print(filename)
        r1=requests.get(imgurl)
        with open(filename,'wb') as f:
            f.write(r1.content)
    time.sleep(1)

# 테이블만들기
# create table car(
#     no number constraint car_no_p primary key,
#     title varchar2(200),
#     price varchar2(200),
#     year varchar2(200),
#     baegi varchar2(200),
#     km varchar2(200),
#     color varchar2(200),
#     trans varchar2(200),
#     garantee varchar2(200),
#     fuel varchar2(200),
#     confirm varchar2(200)
# );
# create sequence car_seq;

#db 연결하기
con=cx_Oracle.connect('happy/day@localhost:1521/xe')
cur=con.cursor()
sql="insert into car values" \
    "(car_seq.nextval,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"

#위에소스 길어보여서 프린트문 제끼고 짧게만듬
url = 'https://www.bobaedream.co.kr/mycar/mycar_list.php?gubun=K&page={}&order=S11&view_size=20'
for page in range(1,2):
    recvd=requests.get(url.format(page))
    dom=BeautifulSoup(recvd.text,'lxml')
    alist=dom.select('#listCont div.mode-cell.title > p.tit > a')
    baseurl='https://www.bobaedream.co.kr'
    urllist=[]
    for a in alist:
        urllist.append(urljoin(baseurl,a['href']))
    for detailurl in urllist:
        r=requests.get(detailurl)
        d=BeautifulSoup(r.text,'lxml')
        title=d.select_one('#bobaeConent div.title-area > h3.tit').text
        price=d.select_one('#bobaeConent div.price-area > span > b').text+'만원'
        imgs=d.select('#bx-pager img')
        imglist=[]

        for img in imgs:
            if(img['src'][2:6]=='file'):
                imglist.append('http:'+img['src'])
        saveImg(imglist,title)
        infos=d.select('#bobaeConent div.info-basic > div > table tr')
        infolist=infos[0].text.strip().split('\n')
        year=infolist[1]
        baegi=infolist[3]
        infolist = infos[1].text.strip().split('\n')
        km=infolist[1]
        color=infolist[3]
        infolist = infos[2].text.strip().split('\n')
        trans=infolist[1]
        garantee=infolist[-1]
        infolist = infos[3].text.strip().split('\n')
        fuel = infolist[1]
        confirm = infolist[-1]
        if confirm=='확인사항':
            confirm=''
        # str="{},{},{},{},{},{},{},{},{},{}"
        # print(str.format(title,price,year,baegi,km,color,trans,garantee,fuel,confirm))
        cur.execute(sql.format(title, price, year, baegi, km, color, trans, garantee, fuel, confirm))
    time.sleep(1)
con.commit()
con.close()

#0318
#실행파일만들기 pyinstaller --onefile bs14-car.py
#자동실행할때는 절!대!경!로!를 써야한다.
#소스바꾸면 실행파일도 새로만든다!!(다시만들면 덮어씌워짐)

# cmd로 할때
# C:\users\admin>d:
# D:\>cd study\pja\dist
# D:\study\pj1\bs\dist>bs14-car

# 에러메세지 : 절대경로를 안써줬을때때# Traceback (most recent call last):
#   File "bs14-car.py", line 112, in <module>
#   File "bs14-car.py", line 65, in saveImg
# FileNotFoundError: [Errno 2] No such file or directory: '..\\car\\르노삼성SM7뉴아트LE23-1.jpg'
# [4288] Failed to execute script bs14-car
