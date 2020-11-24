import pymysql as my
import requests
from bs4 import BeautifulSoup
con=my.connect(host='localhost',
               user='root',
               password='1234',
               db='pythondb',
               charset='utf8')
cur=con.cursor(my.cursors.DictCursor)
sql='insert into movies (title,rate,rsrv,playtime) values (%s,%s,%s,%s)'
url = 'https://movie.naver.com/movie/running/current.nhn'
recvd = requests.get(url)
dom=BeautifulSoup(recvd.text,'lxml')
ul=dom.find('ul',class_='lst_detail_t1')
lis=ul.find_all('li')
for li in lis:
    title = li.find('dt', class_="tit").find('a').text
    rate= li.find('span',class_="num").text
    rsrv = li.find('div', class_="star_t1 b_star")
    if rsrv==None:
        rsrv=''
    else:
        temp=rsrv.find('span',class_="num").text
    rsrv=temp

    play=li.find('dl',class_="info_txt1").text

    playList=play.split('|')
    playtime=''
    for p in playList:
        if p.count('분')==1:
            if p.count('개요')==1:
                p=p.replace('개요','')
            playtime=p.strip()
            break
    cur.execute(sql,(title,rate,rsrv,playtime))
con.commit()
con.close()
