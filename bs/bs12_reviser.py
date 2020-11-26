#제목, 조리순서
import requests
from bs4 import BeautifulSoup

def makeContent(pageUrl):
    with open('data/recette.txt','w',encoding='utf-8') as f:
        r=requests.get(pageUrl)
        d=BeautifulSoup(r.text,'lxml')
        divs=d.find_all('div',class_='view2_summary')
        for div in divs:
            title=div.find('h3').text #제목

        divs2=d.find('div',class_='view_step')
        steps=divs2.find_all('div',class_='media-body')
        i=0
        contents=[]
        for step in steps:
            i=i+1
            contents.append(str(i)+':'+step.text)
            str='{}\n\n조리순서\n{}\n\n\n'.format(title,'\n'.join(contents))
            f.write(str)#join을 왜 넣어줘야하는지

def main(url):
    recvd=requests.get(url)
    dom=BeautifulSoup(recvd.text,'lxml')
    lis=dom.find_all('li',class_='common_sp_list_li')
    for li in lis:
        a = li.find('a')['href']
        pageUrl='https://www.10000recipe.com'+a
        makeContent(pageUrl)


url='https://www.10000recipe.com/recipe/list.html?q=&query=&cat1=&cat2=&cat3=&cat4=63&fct=&order=reco&lastcate=cat4&dsearch=&copyshot=&scrap=&degree=&portion=&time=&niresource='

if __name__=='__main__':
    main(url)