from bs4 import BeautifulSoup

# data추출
#     dom.string
#     dom.text
#     dom.get_text()
# 속성추출
#     dom['속성']
#     dom.get('속성')
#     dom.attrs['속성']
# DOM추적
#     dom.parent 부모
#     dom.parents 조상, 객체로반환
#     dom.children 자식
#     dom.descendants 자손
#     dom.next_siblings 아래쪽 형제요소
#     dom.previous_siblings 위쪽형제요소

with open('data\\test1.html','r',encoding='utf-8') as f:
    txt=f.read()
    #print(txt)
    dom=BeautifulSoup(txt,'lxml')
    # div=dom.find('div')
    # print(div)

    # document object model dom
    # div태그중에 클래스가 'ex_class'인것 첫번째 추출
    # divs=dom.find('div',{'class':'ex_class'})
    # print(divs)

    # div태그중에 클래스가 'ex_class'인것 모두 추출
    # divs = dom.find_all('div', {'class': 'ex_class'})

    #클래스가 'ex_class'인것 모두 추출
    # divs=dom.find_all(class_='ex_class')

    #id는 find_all의 개념이없다.
    # ids = dom.find(id='ex_id')

    #id 'ex_id'인것중 모든 p태그
    # ps=ids.find_all('p')

    # title=dom.find('title')
    # print(title)
    #
    # print(title.string)
    # print(title.text)
    # print(title.get_text())

# 속성추출
    # aes=dom.find_all('a')
    #print(aes)
    # for a in aes:
    #     print(a.text)
    #     print(a['href'])

    # link2=dom.find(id='link2')
    # print(link2.get('class'))


#돔추적-부모
# title=dom.find('p',class_='title')
# print(title)
# print('-'*30)
# print(title.parent)
# print('-'*30)
# print(title.parents)
# print('-'*30)
# for p in title.parents:
#     print(p)
#     print('-' * 30)

#돔추적-자식
#id가 second인 div
div=dom.find(id='second')
# print(div)
# print('-'*30)
# divkid=div.children
# print(divkid)
# for i in divkid: #줄바꿈까지 자식으로 처리
#     print(i)
#     print('!'*30)

# divdes=div.descendants
# print(divdes)
# for i in divdes:
#     print(i)
#     print('-'*30)

#돔추적-형제
a=dom.find(id='link2')
anext=a.next_siblings
print(anext)
for i in anext:
    print(i)
    print('-' * 30)