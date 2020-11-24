# create table music(
#     no number primary key,
#     title varchar2(100),
#     singer varchar2(100),
#     song varchar2(100)
# );
# create sequence music_seq;
# import requests
# from bs4 import BeautifulSoup
# S_PAGENUMBER: 2
# S_MB_CD: W0726200
# S_HNAB_GBN: I
# hanmb_nm: G-DRAGON
# sort_field: SORT_PBCTN_DAY
# import cx_Oracle
# con=cx_Oracle.connect('happy/day@localhost:1521/xe')
# cur=con.cursor()
# sql="insert into music values (music_seq.nextval,'{}','{}','{}')"
# for page in range(1,3):
#     url='https://www.komca.or.kr/srch2/srch_01_popup_mem_right.jsp'
#     data={'S_PAGENUMBER': page,
#     'S_MB_CD': 'W0726200',
#     'S_HNAB_GBN': 'I',
#     'hanmb_nm': 'G-DRAGON',
#     'sort_field': 'SORT_PBCTN_DAY'}
#     recvd=requests.post(url,data=data)
#     # print(recvd)
#     # 1페이지에 있는 저작물명,가수명,작사를 오라클에 저장하세요
#     dom=BeautifulSoup(recvd.text,'lxml')
#     tables=dom.find_all('table')
#     # print(len(tables))   #2
#     trs=tables[1].find_all('tr')
#     # print(len(trs))   #11
#     for i in range(1,len(trs)): #i=1,2,...10
#         tds=trs[i].find_all('td')
#         title=tds[0].text
#         singer=tds[1].text
#         song=tds[2].text
#         # print(title,singer,song)
#         cur.execute(sql.format(title,singer,song))
# con.commit()
# con.close()
# -------------------
# import requests
# from bs4 import BeautifulSoup
# with open('data\\kma.csv','w',encoding='utf-8') as f:
#     url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
#     recvd=requests.get(url)
#     print(recvd.text)
#     # print(recvd)
#     # 서울ㆍ인천ㆍ경기도 서울  기상데이터
#     dom=BeautifulSoup(recvd.text,'lxml')
#     locations=dom.find_all('location')
#     # print(len(locations))
#     for location in locations:
#         province=location.find('province').text
#         city=location.find('city').text
#         # print(province,city)
#         datas=location.find_all('data')
#         for data in datas:
#             mode=data.find('mode').text
#             tmEf=data.find('tmef').text
#             wf=data.find('wf').text
#             tmn=data.find('tmn').text
#             tmx=data.find('tmx').text
#             reliability=data.find('reliability').text
#             rnSt=data.find('rnst').text
#             str='{},{},{},{},{},{},{},{},{}\n'.format(province,city, mode,tmEf,
#                                 wf,tmn,tmx,reliability,rnSt)
#             # print(str)
#             f.write(str)
# --------------
import re    #정규표현식
# str="""
# 3412    Bob 123
# 3834  Jonny 333
# 1248   Kate 634
# 1423   Tony 567
# 2567  Peter 435
# 3567  Alice 535
# 1548  Kerry 534
# """
# re.findall(r'패턴',문자열)
# r1=re.findall('[0-9]',str)
# print(r1)
# r1=re.findall(r'[0-9]+',str)
# r1=re.findall(r'[0-9]+',str)
# print(r1)
# r1=re.findall(r'[A-Z]+',str)
# print(r1)
# r1=re.findall(r'[A-Za-z]+',str)
# print(r1)
# ----------
# *(0번이상),+(1번이상),?(0 또는 1),|(선택)
# [],{1,3} (1번이상 3번이하), {,3}(3번이하),{1,}(1번이상),{3} (3번)
# . 줄바꿈을 제외한 한 글자
print(re.match('a.b','aabrrr'))
print(re.match('a.b','a0brrr'))
print(re.match('a.b','c0brrr'))
print(re.findall('a.b','a0brrr'))
print(re.search('a.b','aabrrr'))
str='3pink dress'
print(re.match('[a-z]+',str))   #문자열 처음부터 정규식과 일치여부
print(re.search('[a-z]+',str)) #문자열 전체를 검색하여 일치여부
print(re.findall('[a-z]+',str)) # 정규식에 일치하는 문자열 반환
# group()정규식에 일치하는 문자열 추출
# print(re.match('[a-z]+',str).group())   #문자열 처음부터 정규식과 일치여부
# print(re.search('[a-z]+',str).group()) #문자열 전체를 검색하여 일치여부
str='pink333 dress444'
print(re.match('[a-z]+',str).group())
print(re.search('[a-z]+',str).group())
print(re.findall('[a-z]+',str))
str='My handphone number 010-3333-7890'
print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d',str))
print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d',str).group())
# print(re.match('\d\d\d-\d\d\d\d-\d\d\d\d',str).group())
print(re.findall('\d\d\d-\d\d\d\d-\d\d\d\d',str))
print(re.search('[0-9]{3,4}-[0-9]{3,4}-[0-9]{3,4}',str).group())
print('\n\n\n\n\n\n\n\n')
# 클래스 -





# 정규식








