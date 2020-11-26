import requests
from bs4 import BeautifulSoup
def saveImg(imgUrl,title):
    # print(imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]) #imgUrl[92:96]
    # print(title)
    title=title.replace('[','')
    title = title.replace(']', '')
    title = title.replace("'", '')
    title = title.replace("?", '')
    title = title.replace(",", '')
    filename='../img/'+title+imgUrl[imgUrl.index('?')-4:imgUrl.index('?')]
    # print(filename)
    r=requests.get(imgUrl)
    f=open(filename,'wb')
    f.write(r.content)
    f.close()
def makeData(pageUrl):
    r=requests.get(pageUrl)
    d=BeautifulSoup(r.text,'lxml')
    imgUrl=d.find('div',id='newsEndContents').find('img')['src']
    title=d.find('h4').text
    saveImg(imgUrl,title)
    content=d.find('div',id='newsEndContents')
    str='{}::\n{}\n'.format(title,content)
    with open('../data/sports2.cvs','w',encoding='utf-8') as a:
        a.write(str)
url='https://sports.news.naver.com/index.nhn'
recvd=requests.get(url)
dom=BeautifulSoup(recvd.text,'lxml')
aes=dom.find_all('a',class_='link_today')
for a in aes:
    pageUrl='https://sports.news.naver.com'+a['href']
    print(a['href'])
    # makeData(pageUrl)