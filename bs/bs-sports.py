import requests
import json
with open('d:\\study\\pj1\\data\\sports.csv','a',encoding='utf-8') as f:
    url='https://sports.news.naver.com/wfootball/news/list.nhn?isphoto=N'
    recvd=requests.get(url)
    dic=json.loads(recvd.text)
    for i in dic['list']:
        str='{}::{}\n'.format(i['title'],i['subContent'])
        f.write(str)
#--------------
#터미널에 pip install pyinstaller
# (venv) D:\study\pj1>pyinstaller bs-sports.py   X
# (venv) D:\study\pj1> cd bs > pyinstaller --onefile bs-sports.py 이렇게해야 에러안생기고 깔끔하게됨
# 소스가 변경되면 exe파일 새로만들어야함

# 윈도우+r - cmd
# C:\Users\admin>d:
# D:\>cd D:\study\pj1\bs\dist
# D:\study\pj1\bs\dist>sports.exe

# 정기 프로그램 설정
# 제어판 > 시스템및보안 > 관리도구 > 작업스케쥴러 > 동작 > 기본작업만들기