#한국저작물협회 > 저작자 저작물 조회 >
# 1페이지에 있는 저작물명, 가수명, 작사를 오라클에 저장
import requests
from bs4 import BeautifulSoup
import cx_Oracle
#network > srch_01_popup_mem_right.jsp > headers> formdata
      # S_PAGENUMBER: 1
      # S_MB_CD: W0115500
      # S_HNAB_GBN: I
      # hanmb_nm: 이상은
      # sort_field: SORT_PBCTN_DAY

con=cx_Oracle.connect('happy/day@localhost:1521/xe')
cur=con.cursor()

# create table songs(
#     no number primary key,
#     title varchar2(100),
#     singer varchar2(20),
#     writer varchar2(20)
# );
# create sequence songs_seq;
# insert into songs values(webtoon_seq.nextval,'제목','가수','작사');
sql="insert into songs values(songs_seq.nextval,'{}','{}','{}')"
for page in range(1,3):
      url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
      data={'S_PAGENUMBER': page,
            'S_MB_CD': 'W0115500',
            'S_HNAB_GBN': 'I',
            'hanmb_nm': '이상은',
            'sort_field': 'SORT_PBCTN_DAY'}
      recvd = requests.post(url,data=data)
      dom = BeautifulSoup(recvd.text,'lxml')

      # tr=dom.find_all('tr')

      # for i in range(2,len(tr)): 내가한거
      #       title=tr[i].find('td').string
      #       singer=tr[i].select('td')[1].text
      #       writer=tr[i].select('td')[2].text
      #       cur.execute(sql.format(title,singer,writer))
      # con.commit()
      # con.close()
      #-------------------------------------------------
      tables=dom.find_all('table')
      # print(len(tables)) #2
      trs=tables[1].find_all('tr')
      # print(len(trs)) #11
      for i in range(1,len(trs)):
           tds = trs[i].find_all('td')
           title=tds[0].text
           singer=tds[1].text
           if (len(singer)<20):
                 singer=singer[:4]
           writer=tds[2].text
           if writer=='':
                 writer='이상은'
           print(title,singer,writer)
#            cur.execute(sql.format(title, singer, writer))
# con.commit()
# con.close()