import json
import os
import sys
import urllib.request
with open('../data/iHaveADream.txt','r') as f:
    txt=f.read()
    print(txt)
client_id = "P5NC3PzLiI6T454duFcX"
client_secret = "XsmZUUqUp0"
encText = urllib.parse.quote(txt)
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if (rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
    # i have a dream을 검색해 한국어로 번역
    # 안보이는 특수한 문자들때문에 안됨
