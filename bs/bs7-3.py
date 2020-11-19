import os
import sys
import urllib.request
import json
client_id = "b3sD4mEfhUBH9gHc8DCt"
client_secret = "2SmGkrIAOp"
encText = urllib.parse.quote("빌리아일리시")
url = "https://openapi.naver.com/v1/search/blog?start=101&display=100&query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result=response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)
dic=json.loads(result)
print(dic)