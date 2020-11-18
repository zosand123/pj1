# def f1(n):
#     return n*10
# print(f1(4))
# a=f1
# print(a(7))

#람다함수 : 메모리절약, 가독성향상, 간결한코드
#lambda 매개변수:반환값
# b=lambda n:n*10
# print(b(1))
# def f2(x,y,f):          #f=lambda x:x+1
#     print(x*y*f(x+y))   #10+100+f(110)
# f2(10,100,lambda f:f+1)

# a=[1,2,3,4,5] #-->[3, 6, 9, 12, 15]
# def f3(x):
#     result=[]
#     for i in x:
#         result.append(i*3)
#     return result
# print(f3(a))

#map(함수,반복가능객체):매개변수로 함수와 반복가능객체를 입력
# def f4(x):
#     return x*3
# print(f4(7))
# #오류 print(f4[1,2,3,4])
# print(f4([1,2,3,4])) #[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# print(map(f4,[1,2,3,4])) #<map object at 0x00000073B8E182B0>
# print(list(map(f4,[1,2,3,4]))) #list로 형변환해줘야 [3, 6, 9, 12]
# print(list(map(lambda n:n*3,[1,2,3,4]))) #동일

import os
import glob
#파일경로 리눅스, 맥에서는 / 윈도우는 \
#os 모듈: 디렉토리, 파일등의 os자원 제어
#glob모듈
# print('현재 작업디렉토리',os.getcwd())  #current working directory
# print('현재 작업디렉토리의 목록',os.listdir())
# print('d:\목록',os.listdir('d:\\'))
# print(os.listdir('D:\\down\\erd'))
# print(os.path.join('..','test1'))  #경로생성
# print(os.listdir(os.path.join('..','test1')))
# print(os.path.join('..','test1','Scripts'))
# with open('data\\webtoon.csv','w',encoding='utf-8') as f:
#     pass
# with open(os.path.join('data','webtoon.csv'),'w',encoding='utf-8') as f:
#     pass

# print(glob.glob('*')) #현재폴더에있는 모든 파일 []로 반환
# print(glob.glob('*.py')) #현재폴더에있는 모든 파일중 확장자가 py인것만 []로 반환
# f1='D:/study/pj1/data/Beauty.smi'
# print(os.path.dirname(f1))
# print(os.path.basename(f1)) #가장 마지막에 있는 이름(파일이든 디렉토리든)

# f=open(os.path.join('..','data','Beauty.smi'))
# #print(f.read())
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line,end="")
# f.close()

#data폴더의 모든파일 내용출력
# filelist=glob.glob(os.path.join('..','data','*'))
# print(filelist)
# for file in filelist:
#     with open(file,encoding='utf-8') as f:
#         print(os.path.basename(file))
#         if os.path.basename(file)!='io2.py':
#             print(f.read())
#             print('-'*30)
#smi파일 인코딩때문에 실행안돼서 메모장으로 다시 저장해서 인코딩 utf-8로 바꿨더니 실행됨

#Beauty.smi --> [자막만] --> Beauty.txt로 바꾸기
def makeTxt(inputFile):
    f=open(inputFile,encoding='utf-8')
    result=[]
    for line in f:
        line=line.replace('\n','')
        if len(line)<4:
            continue
        elif line.count(':')>3:
            continue
        line=line.replace('<b>','')
        line = line.replace('</b>', '')
        line = line.replace('<i>', '')
        line = line.replace('</i>', '')
        result.append(line)
    f.close()
    return result

def makeFile(inputFile,temp):
    fileName=inputFile[:-3]+'txt'
    with open(fileName,'w',encoding='utf-8') as fw:
        for t in temp:
            fw.write(t+'\n')

def main():
    inputFile='../data/Beauty.smi'
    temp=makeTxt(inputFile)
    makeFile(inputFile,temp)

if __name__=='__main__': #다른파일에서 실행된내용은 못가져가게 하기위함
    main()
