# import basic
# logger=basic.logger
# def hap(n):
#     logger.info('hap함수 호출')
#     h=0
#     for i in range(n+1):
#         h=h+i
#         if h>1000:
#             logger.critical("합이 1000을 초과,"+str(i)+","+str(h))
#     return h
# print(hap(10))
# print(hap(100))
# ---예외처리--------------------
# try:
#     예외가 발생할 가능성이 있는 코드
# except 예외명1:
#     코드
# except 예외명2:
#     코드
# else:       #예외가 없을 경우 실행
#     코드
# finally:
#     코드
# names=['kim','lee','park']
# try:
#     # i='lee'
#     i='park'
#     # i='choi'
#     print(names.index(i))
#     x=[1,2]
#     y='test'
#     z=x+y
# except ValueError:
#     print('해당값이 리스트에 없음')
# except TypeError:
#     print('리스트와 문자열을 연결못함')
# except:
#     print('예외발생')
# else:
#     print('ok')
# finally:
#     print('무조건 실행')
# yield -----------------------------
# n=[1,2,3,4,5]
# rn=reversed(n)
# print(rn)
#이터러블:리스트,문자열,튜플,딕션어리처럼 요소를 차례차례 꺼낼수 있는 객체
# for c in 'python':
#     print(c)
# 이터레이터:이터러블 중에서 next()함수를 사용해서 요소를 하나하나 꺼낼수 있는 객체
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(n))
# for i in rn:
#     # print(99)
#     # print(next(i))   오류
#     print(i)
# def test():
#     print('test함수 호출')
#     yield 'test'
# print('a')
# test()
# print('b')
# test()
# print(test())
# 제너레이터 함수:제너레이터를 리턴하는 함수
# yield까지만 실행
# 제너레이터 next()함수를 이용하여 함수의 내부 코드 실행

def test1():
    print('one')
    yield 11
    print('two')
    yield 22
    print('three')
r1=test1()
print('four')
r2=next(test1())
print(r2)
for i in test1():
    print(i)
#아나콘다설치, 가상환경설정, 스크래피설정, 쥬피터노트북 사용법
#http://copycoding.tistory.com/60 #텐서플로우가 cpu특성을 탄다 텐서플로우와 호환하기위해 구버전을 다운받는다