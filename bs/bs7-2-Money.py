import requests
import json
from fake_useragent import UserAgent #바로 못들어가는 url을 속여 들어갈수있게함
ua=UserAgent() #자바로 표현하자면 UserAgent ua=new UserAgent()
# print(ua.chrome)
# print(ua.ie)
headers={'user-agent':ua.chrome,'referer':'https://finance.daum.net'}
# url='https://finance.daum.net' -referer
url='https://finance.daum.net/api/search/ranks?limit=10' #진짜url
recvd=requests.get(url,headers=headers)
dic=json.loads(recvd.text)
with open('../data/money.csv','w',encoding='utf-8') as f:
    for i in dic['data']:
        f.write('{},{},{}\n'.format(i['rank'],i['name'],i['tradePrice']))



#referer : 거쳐야하는 url
#엑셀로 처리할거면 인코딩을 지운다