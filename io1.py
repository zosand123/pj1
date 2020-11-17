#open('파일명',모드)
#사용
#변수.close() 자원반납
#모드 : r(읽기) : 디폴트 ,w(쓰기) : 지우고 새로써짐 ,a(추가) : 없으면 만들고 있으면 덧붙이고

#f=open('d:\study\pj1\data\les_phares.txt','r',encoding='utf-8')
# f=open('data/les_phares.txt',encoding='utf-8') #같은 위치에 있어서 파일명만 입력
# txt=f.read() #전체내용읽기
#txt=f.read(5) #5글자 읽기
# print(txt)
# print(type(txt)) #<class 'str'>
# f.close()

# f=open('data/les_phares.txt',encoding='utf-8')
# txt=f.readline() # 한줄읽기
# print(txt)
# print(type(txt)) #<class 'str'>
# f.close()

# f=open('data/les_phares.txt',encoding='utf-8')
# txt=f.readlines() # 한줄씩 모두 다읽기, 줄단위 리스트 반환
# print(txt)
# print(type(txt)) #<class 'list'>
# for line in txt:
#     print(line.strip()) #strip() 공백제거
# f.close()

#with open('파일명',모드) as 변수명: with 블럭이 끝날때 자동 close
# with open('data/les_phares.txt',encoding='utf-8') as f:
#     txt=f.read()
#     print(txt)

# with open('data/test1.txt','w',encoding='utf-8') as f:
#     f.write('홍준씨 연락왔어요?\n')

# with open('data/test1.txt','a',encoding='utf-8') as f:
#     for i in range(100):
#         f.write(str(i)+'\n')

# fruit=['사과','배','포도']
# with open('data/text2.txt','a',encoding='utf-8') as f:
#     # for a in fruit:
#     #     f.write(a)
#     f.writelines(fruit) #리스트를 파일에 쓰기. 위와 동일

# with open('data/test1.txt','w') as f:
#     print('test print', file=f) #write랑 똑같고 잘안씀

# col=['이름','나이','주소']
# names=['홍길동','심청','이몽룡','성춘향']
# age=[20,16,16,16]
# juso=['서울','서산','남원','진주']
# with open('data/addr.txt','w',encoding='utf-8') as f:
#     f.write(','.join(col)+'\n')
#     for i in range(len(names)): #i=0,1,2,3
#         str='{},{},{}\n'.format(names[i],age[i],juso[i])
#         f.write(str)

# a=['one','two','three']
# #'연결문자'.join(리스트)
# print('-'.join(a))
# print('?'.join(a))
# print(type('?'.join(a)))

#이미지저장
# import requests #웹서버에 접근하는 모듈, 설치해야함 file>settings>python interpreter>+표시 클릭
# url='https://shared-comic.pstatic.net/thumb/webtoon/739350/thumbnail/thumbnail_IMAG06_22912ab6-2209-4f31-971d-c0bf191e14d7.jpg'
# recvd=requests.get(url)
# # print(recvd) #  <Response [200]> 2xx (성공): 요청을 성공적으로 받았으며 인식했고 수용하였다
# with open('img/webtoon.jpg','wb') as f: #이미지는 이진파일이기때문에 write binary 줄여서 wb라고 써야함
#      f.write(recvd.content)

# import requests
# url='https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbLaXCL%2FbtqAmtAGFET%2Fd2RFW2HLeVboHktC0rHXSK%2Fimg.png'
# recvd=requests.get(url)
# print(recvd)
# with open('img/1.jpg','wb') as f:
#      f.write(recvd.content)