import requests
from bs4 import BeautifulSoup
#영화제목 점수 예매율, 상영시간을 추출하여 data\\movie.csv 저장
#영화포스터는 img폴더에 저장

# def saveImg(imgUrl,title):
#     print(imgUrl)
#     print(imgUrl.index('?'))
#     print(imgUrl[79:83])
#     print(imgUrl[imgUrl.index('?')-4:imgUrl.index('?')])
#     filename='../img/'+title+imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]
#     print(filename)

# url = 'https://movie.naver.com/movie/running/current.nhn#'
# recvd = requests.get(url)
# # print(recvd.text)
# dom=BeautifulSoup(recvd.text,'lxml') #파싱
# ul=dom.find('ul',class_='lst_detail_t1')
# lis=ul.find_all('li')
# # print(len(lis))
# for li in lis:
#     img=li.find('img')['src']
#     # print(img)
#     title = li.find('dt', class_="tit").find('a').text
#     # print(title)
#     rate= li.find('span',class_="num").text
#     # print(rate)
#
#     # rsrv=li.find('div',class_="star_t1 b_star").find('span',class_="num").text
#     # 예매율이 없는경우에 에러가생겨서 if문 추가
#     rsrv = li.find('div', class_="star_t1 b_star")
#     if rsrv==None:
#         rsrv=''
#     else:
#         temp=rsrv.find('span',class_="num").text
#     rsrv=temp
#
#     play=li.find('dl',class_="info_txt1").text
#
#     playList=play.split('|')
#     playtime=''
#     for p in playList:
#         if p.count('분')==1:
#             if p.count('개요')==1:
#                 p=p.replace('개요','')
#             playtime=p.strip()
#             break
#     str='%s,%s,%s,%s'%(title,rate,rsrv,playtime)
#     print(str)
#------------------------------------------------------------------
import os
def saveImg(imgUrl,title):
    title=title.replace(':','')
    filename='../img2/'+title+imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]
    #print(filename)
    r=requests.get(imgUrl)
    with open (filename,'wb') as f1:
        f1.write(r.content)

with open(os.path.join('..','data','movies.csv'),'w',encoding='utf-8') as f:
    url = 'https://movie.naver.com/movie/running/current.nhn#'
    recvd = requests.get(url)
    dom=BeautifulSoup(recvd.text,'lxml')
    ul=dom.find('ul',class_='lst_detail_t1')
    lis=ul.find_all('li')
    for li in lis:
        img=li.find('img')['src']
        title = li.find('dt', class_="tit").find('a').text
        saveImg(img,title)
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
        str='%s,%s,%s,%s\n'%(title,rate,rsrv,playtime)
        f.write(str)



# # apple을 꺼내오기
# a='777 |    apple        | 곰분 | 아아아아'
# print(a.split('|')[1].strip())
# #분의 갯수세기
# for s in a.split('|'):
#     print(s,s.count('분'))