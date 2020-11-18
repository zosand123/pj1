#함수를 다 가지고오면 파일명.함수명
#함수만 가지고오면 함수명으로 바로접근

# import calc
# print(calc.add(3,4))
# print(calc.mul(3,4))
# print(calc.sub(3,4))

# from calc import add,sub
# print(add(10,100))
# print(sub(5,1))
#print(mul(5,1)) 안가져와서 사용X

from calc import add as a,sub as s #함수명에 별칭주기
print(a(10,100))
print(s(5,1))
