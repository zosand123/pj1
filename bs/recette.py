import requests
from bs4 import BeautifulSoup
# # import re
# #만개의 레시피에서 밑반찬레시피를 recipe.txt 로 저장
#
# def makeData(pageUrl):
#     r=requests.get(pageUrl)
#     d=BeautifulSoup(r.text,'lxml')
    # tDivs=d.find_all('div',class_='view2_summary')
    # for div in tDivs:
    #     title=div.find('h3').text
    #     print(title)
    #
    # view_step = d.find('div',class_='view_step')
    # divs=view_step.find_all('div',class_='media-body')
    # # print(divs)
    # for div in divs:
    #     print(div.text)

    # while(len(cDivs)):
    #     content=cDivs.text
    #     print(content)
    # with open('../data/recipe.txt','w',encoding='utf-8') as f:
    #     f.write('{}\n{}'.format(title,content))

    # i=0
    # for div in divs:
    #     i++
    #     print(str(i)+)
# url='https://www.10000recipe.com'
# recvd=requests.get(url)
# dom=BeautifulSoup(recvd.text,'lxml')
# aes=dom.find_all('a',class_="common_sp_link") 이렇게 바로 처가니까 이상한데로 나옴
# for a in aes:
#     if((len(a['href']))<16):
#         pageUrl = url + a['href']
#         print(pageUrl)
#         makeData(pageUrl)
#         break

#-----------------------------------------------------------------
def makeContent(pageUrl):
    pass
def main(url):
    url='https://www.10000recipe.com/recipe/list.html?q=%EB%B0%91%EB%B0%98%EC%B0%AC'
    r=requests.get(url)
    dom=BeautifulSoup(r.text,'lxml')
    lis=dom.find_all('li',class_="common_sp_list_li")
    print(len(lis))
    for li in lis:
        pageUrl='https://www.10000recipe.com'+li.find('a')['href']
        print(pageUrl)

        break


if __name__=='__main__':
    main(url)



