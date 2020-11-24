import requests
from bs4 import BeautifulSoup
import cx_Oracle
con=cx_Oracle.connect('happy/day@localhost:1521/xe')
cur=con.cursor()
#sql='insert into webtoon values(webtoon_seq.nextval,:1,:2,:3)'
sql="insert into webtoon values(webtoon_seq.nextval,'{}','{}','{}')" #어떤 db이든 실행될수있게.
# create table webtoon(
#     no number primary key,
#     title varchar2(100),
#     rating varchar2(20),
#     regdate varchar2(20)
# )
# create sequence webtoon_seq;
# insert into webtoon values(webtoon_seq.nextval,'제목','평점','등록일');

for page in range(1,5):
    pageurl='https://comic.naver.com/webtoon/list.nhn?titleId=739350&weekday=fri&page={}'.format(page)
    recvd=requests.get(pageurl)
    dom=BeautifulSoup(recvd.text,'lxml')
    table=dom.find('table',class_="viewList")
    trs=table.find_all('tr')
    for i in range(2,len(trs)):
        td1=trs[i].find('td',class_='title')
        title=td1.find('a').text #제목
        div=trs[i].find('div',class_='rating_type')
        rate=div.find('strong').text #별점
        date=trs[i].find('td',class_='num').text #날짜
        # cur.execute(sql,(title,rate,date))
        cur.execute(sql.format(title,rate,date)) #어떤 db이든 실행될수있게.
con.commit()
con.close()

