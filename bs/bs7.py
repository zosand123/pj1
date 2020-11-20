import requests
import json
with open('data\\sports.csv','w',encoding='utf-8') as f:
    # url='https://sports.news.naver.com/wfootball/news/index.nhn?isphoto=N'
    url='https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
    recvd=requests.get(url)
    # print(recvd)
    # print(recvd.text)
    dic=json.loads(recvd.text)
    # print(dic)
    # print(dic['list'])    #[{},{},{},....]
    # 기사제목, 내용을 출력
    for i in dic['list']:  #i={},{},...
        str='{}::{}\n'.format(i['title'],i['subContent'])
        f.write(str)
print('-'*30)
import requests
from fake_useragent import UserAgent
import json
ua=UserAgent()   # UserAgent ua=new UserAgent()
# print(ua.chrome)
# print(ua.ie)
with open('data\\money.csv','w',encoding='utf-8') as f:
# with open('data\\money.csv', 'w') as f:
    headers={'user-agent':ua.chrome,
             'referer': 'https://finance.daum.net/'}
    url='https://finance.daum.net/api/search/ranks?limit=10'
    recvd=requests.get(url,headers=headers)
    # print(recvd)
    # print(recvd.text)
    dic=json.loads(recvd.text)
    for i in dic['data']:
        str='{},{},{}\n'.format(i['rank'],i['name'],i['changePrice'])
        f.write(str)










