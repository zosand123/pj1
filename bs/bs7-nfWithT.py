import json
import os
import sys
import urllib.request
client_id = "b3sD4mEfhUBH9gHc8DCt"
client_secret = "2SmGkrIAOp"
encText = urllib.parse.quote("넷플릭스")
with open('../data/blog.csv','a',encoding='utf-8') as f:
    for i in range(1,902,100):
        url = "https://openapi.naver.com/v1/search/blog?start={}&display=100&query=" + encText # json 결과

        request = urllib.request.Request(url.format(i))
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result=response_body.decode('utf-8')
        else:
            print("Error Code:" + rescode)
        dic = json.loads(result)
        for d in dic['items']:
            str='{}::{}\n'.format(d['title'],d['description'])
            f.write(str)

   