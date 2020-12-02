from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #특수키사용
#자바스크립트 실행 execute_script()
# driver=webdriver.Chrome('data\\chromedriver')
# url='https://www.10000recipe.com/recipe/list.html'
# driver.get(url) # 해당페이지 접속
# driver.execute_script('alert("happy day")') #js쓰기

#만개의 레시피 #자바스크립트로 돼있을때 스크립트 실행
# a2=driver.find_element_by_css_selector('#id_search_category div.cate_list > a:nth-child(2)')
# print(a2.text)
# print(a2.get_attribute('href'))
# driver.execute_script(a2.get_attribute('href'))

#이미지 urllib.request로 다운받기
# import urllib.request
# imgUrl="https://shared-comic.pstatic.net/thumb/webtoon/739350/thumbnail/thumbnail_IMAG10_cc92f13a-56b6-415e-a5d3-37c34bad2bdd.jpg"
# filename='img/web1.jpg'
# urllib.request.urlretrieve(imgUrl,filename)

#상대경로를 절대경로로 바꿔줄때 쓰는 parser
# from urllib.parse import urlparse
# url='http://www.ml5.co.kr:1621/a502/index.html?student=14&area=60'
# pr=urlparse(url)  #named tuple 반환 : key값을 가진 튜플
# print(pr)
# print(pr.scheme) #http.ftp....
# print(pr.path) #/a502/index.html
# print(pr.netloc) #네트웍위치
# print(pr.query) #물음표뒤의 값

#url 바꿔줄때
# from urllib.parse import urljoin
# baseurl='https://www.ml5.co.kr:1621/green/a502/index.html'
# print(1, urljoin(baseurl,'1.html'))
# print(2, urljoin(baseurl,'b.html'))
# print(3, urljoin(baseurl,'/c.html'))
# print(4, urljoin(baseurl,'//d.html'))
# print(5, urljoin(baseurl,'blue/e.html'))
# print(6, urljoin(baseurl,'../blue/index.html'))
# print(7, urljoin(baseurl,'http://f.html'))

import os
# filename='D:\study\pj1\data\Beauty.txt'
# name1=os.path.join('D:\\','study','pj1','data','Beauty.txt')
# name2=os.path.join('D:\\','study','pj1','data')
# print(os.path.dirname(name1))
# print(os.path.basename(name1)) #파일명
# print(os.path.dirname(name2))
# print(os.path.basename(name2)) #파일명
# print(os.path.exists('d:\\study\\pj1\\data'))
# print(os.path.exists('d:\\study\\pj1\\data2'))
# if not os.path.exists('d:\\study\\pj1\\data2'): #디렉토리 만들기
#     os.mkdir('d:\\study\\pj1\\data2')
a=[i for i in range(5)]
print(a)
b=['one','two','three']
print(b)
c=a+b
print(c)
a.append(b) #덩어리째 요소로 들어옴
print(a)