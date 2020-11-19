#넷플릭스로 1000건 검색하여 제목과 상세내용을 blog.csv로 저장

import os
import sys
import urllib.request
client_id = "b3sD4mEfhUBH9gHc8DCt"
client_secret = "2SmGkrIAOp"
encText = urllib.parse.quote("넷플릭스")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result=response_body.decode('utf-8')
    print(result)
else:
    print("Error Code:" + rescode)
