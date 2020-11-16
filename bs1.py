#import bs4 #안에있는거 다가져오기
import requests
# url='https://www.naver.com'
# recvd=requests.get(url)
# print(recvd)
# # print(recvd.text) #html 코드
# print(recvd.encoding)
# print(recvd.headers)

from bs4 import BeautifulSoup #BeautifulSoup만 가져오기
#웹페이지에 접근하여 태그인식
f=open('data/test1.html',encoding='utf-8').read()
# print(f)
# BeautifulSoup(웹페이지,파싱방식)

# 파싱(태그를 인식하고 부족한거 채워줌):html.parser,html5lib,lxml(제일빠름)
# dom=BeautifulSoup(f,'html.parser')
dom=BeautifulSoup(f,'lxml')
#print(dom)

# 특정태그가져오기 : dom.find('태그') = #dom.태그

# div=dom.find('div') #첫번째 div 태그 가져옴
# div=dom.div
# print(div)

# 모든태그 추출,리스트로 반환 : dom.find_all('태그')
# divs=dom.find_all('div')
# print(divs)

# firstdiv=dom.div
# div2=firstdiv.div
# print(div2)
# ps=div2.find_all('p')
# print(ps)

# dom.find(['태그'],class_='클래스명') #예약어 피하기 위해 _붙여줌
# dom.find('태그',{'class':'클래스명'})
# cl=dom.find('div',class_='ex_class')
# print(cl)
# dom.find_all(['태그'],class_='클래스명')
# dom.find_all('태그',{'class':'클래스명'})
#exs=dom.find_all(class_='ex_class')
# exs=dom.find_all('all',{'class':'ex_class'})
# print(exs)

#클래스가 sister인 모든 태그
# sisters=dom.find_all(class_='sister')
# print(sisters)
#
#id가 third인 모든 태그
thirds=dom.find_all(id='third')
# print(thirds)

#id가 third인 모든 태그의 첫번째 p태그
# print(thirds[0])
p1=thirds[0].find('p')
print(p1)