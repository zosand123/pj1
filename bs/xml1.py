import requests
from bs4 import BeautifulSoup
with open('../data/climat.csv','w',encoding='utf-8') as f:
    url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
    recvd=requests.get(url)
    dom=BeautifulSoup(recvd.text,'lxml')
    #서울.인천.경기도
    locations=dom.find_all('location')
    # print(len(locations)) #41
    for location in locations:
        province=location.find('province').text
        city=location.find('city').text
        # print(province,city)
        datas=location.find_all('data')
        for data in datas:
            mode=data.find('mode').text
            tmEf=data.find('tmef').text #실제태그 대문자섞여있어도 찾을 때는 소문자로 찾아야함
            wf=data.find('wf').text
            tmn=data.find('tmn').text
            tmx=data.find('tmx').text
            reliability=data.find('reliability').text
            rnSt=data.find('rnst').text
            str='{},{},{},{},{},{},{},{},{}\n'.format(province,city,
                              mode,tmEf,wf,tmn,tmx,reliability,rnSt)
            f.write(str)
#정규표현식-----------------------------
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
# print(re.match('a.b','aabrrr'))
# print(re.match('a.b','a0brrr'))
# print(re.match('a.b','c0brrr'))
# print(re.findall('a.b','a0brrr'))
# print(re.search('a.b','aabrrr'))
# str='3pink dress'
# print(re.match('[a-z]+',str))   #문자열 처음부터 정규식과 일치여부
# print(re.search('[a-z]+',str)) #문자열 전체를 검색하여 일치여부
# print(re.findall('[a-z]+',str)) # 정규식에 일치하는 문자열 반환
# # group()정규식에 일치하는 문자열 추출
# # print(re.match('[a-z]+',str).group())   #문자열 처음부터 정규식과 일치여부
# # print(re.search('[a-z]+',str).group()) #문자열 전체를 검색하여 일치여부
# str='pink333 dress444'
# print(re.match('[a-z]+',str).group())
# print(re.search('[a-z]+',str).group())
# print(re.findall('[a-z]+',str))
# str='My handphone number 010-3333-7890'
# print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d',str))
# print(re.search('\d\d\d-\d\d\d\d-\d\d\d\d',str).group())
# # print(re.match('\d\d\d-\d\d\d\d-\d\d\d\d',str).group())
# print(re.findall('\d\d\d-\d\d\d\d-\d\d\d\d',str))
# print(re.search('[0-9]{3,4}-[0-9]{3,4}-[0-9]{3,4}',str).group())

#---
#옵션
# re.I or re.IGNORECASE>대소문자상관X
# re.DOTALL or re.S :줄바꿈포함
# re.VERBOSE or re.X :정규식에 주석을 사용할 수 있다
# str="""
# 3412    Bob 123
# 3834  Jonny 333
# 1248   Kate 634
# 1423   Tony 567
# 2567  Peter 435
# 3567  Alice 535
# 1548  Kerry 534
# """
# print(re.findall('[a-z]+',str,re.I)) #옵션re.I>대소문자상관없이
# t1=re.compile('[a-z]+'.re.I)
# print(t1.findall(str))
#-------------------------------------
# import pyperclip #clipboard를 제어하는 오듈
#pyperclip.copy('hello python!') #실행하면 복사됨
# print(pyperclip.paste())
#---------------------------------------
#https://namu.wiki/w/%EC%9D%B4%EB%A9%94%EC%9D%BC
# import pyperclip #clipboard를 제어하는 오듈
# #pyperclip.copy('hello python!') #실행하면 복사됨
# email_regex=re.compile(r'''(
#     [a-zA-Z0-9_.-]+ #username
#     @
#     [a-zA-Z0-9.-]+   #도메인
#     (\.[a-zA-Z]{2,4}){1,2} #com or co.kr
# )''',re.VERBOSE)
# text=pyperclip.paste()
# result=email_regex.findall(text)
# for r in result:
#     print(r[0])

#------------------------------

f=open('../data/test1.html',encoding='utf-8')
text=f.read()
# tag=re.compile('<.+>') #탐욕적방식 : 태그 묶음으로 찾아줌
tag=re.compile('<.+?>') #게으른 방식 : 태그 다 떼서 찾아줌
# print(tag.match(text))
# print(tag.search(text))
print(tag.findall(text))
tag=re.compile('<(.+?)>') #괄호안에것만 찾아줌
print(tag.findall(text))

#---------------------------------------------

# str='internationalization'
# # test=re.compile(r'i.+n') #탐욕적방식
# test=re.compile(r'i.+?n') #게으른방식 - 개별적으로 찾고싶을때
# print(test.findall(str))
