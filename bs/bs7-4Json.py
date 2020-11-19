import requests
import json

with open('../data/sports.csv','w',encoding='utf-8') as f:
    url='https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
    recevd=requests.get(url)
    # print(recevd.text)
    dic=json.loads(recevd.text)
    # print(dic)

    #기사제목, 내용 출력
    # print(dic['list'])
    for i in dic['list']: #i={},{}
        str='{}::\n{}\n\n'.format(i['title'],i['subContent'])
        f.write(str)

#url로 원하는내용을 가져올수없을때는 f12 > network에 가서 Name을 하나하나 클릭해서
# preview를 보고 내가 원하는 데이터를 가진 url를 하나하나 찾는다