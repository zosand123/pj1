# class 클래스명:
#     메서드
#     메서드
# class Car:
#     def __init__(self,t,c):
#         print('생성자')
#         self.type=t
#         self.color=c
#     def showInfo(self):
#         print(self.type+','+self.color)
#     def turing(self,c):
#         self.color=c
#         self.showInfo()
#     def __del__(self):
#         print('소멸자')
# c1=Car('suv','은색')
# c1.showInfo()
# c1.turing('검은색')
# c2=Car()

# 다중상속----------------------------------
# class X(object):
#     pass
# class Y:
#     pass
# class Z():
#     pass
# # print('상속관계:',X.mro())
# # print('상속관계:',Y.mro())
# # print('상속관계:',Z.mro())
# class A(X,Y):
#     pass
# class B(Y,Z):
#     pass
# class D(A,B,Z):
#     pass
# # print('상속관계:',A.mro())
# # print('상속관계:',D.mro()) # 너무 복잡한 다중상속은 코드해석이 어려워서 지양
# class Car:
#     def __init__(self,type,color):
#         self.type=type
#         self.color=color
#     def show(self):
#         print('Car class show 메서드',self.type,self.color)
#
# class KiaCar(Car):
#     def __init__(self,carname,type,color):
#         super().__init__(type,color) #부모생성자 호출
#         self.carname=carname
#     def show(self): #부모함수 재정의
#         print('KiaCar class show 메서드',self.type,self.color,self.carname)
#     def tuning(self,color):
#         self.color=color
#
# class HyundaeCar(Car):
#     def __init__(self,carname,type,color):
#         super().__init__(type,color)
#         self.carname=carname
#
# k1=KiaCar('k9','세단','white')
# k1.show()
# k1.tuning('yellow')
# k1.show()         #인스턴스 메서드 호출
# print(k1.carname) #객체 속성에 접근
# h1=HyundaeCar('제네시스','세단','gray')
# h1.show()

#---------------------------------------------------
import cx_Oracle
class DBManager:
    def __init__(self):
        self.con=cx_Oracle.connect('happy/day@localhost:1521/xe')
        self.cur=self.con.cursor()
        # self.cur.rowfactory = lambda *args: dict(zip([d[0] for d in self.cur.description], args))
        print('연결성공')
    def __del__(self):
        print('연결해제')
        self.con.close()
    def selectAll(self):
        sql="select * from webtoon order by no"
        self.cur.execute(sql)
        rows=self.cur.fetchall()
        for row in rows:
            print(row)
    def selectJob(self):
        pass
    def selectRating(self,rating):
        sql = "select * from webtoon where rating>={}"
        self.cur.execute(sql.format(rating))
        rows = self.cur.fetchall()
        for row in rows:
            print(row[0], row[1], row[2], row[3])
    def insert(self,title,rating,regdate):
        sql="insert into webtoon values (webtoon_seq.nextval,'{}','{}','{}')"
        self.cur.execute(sql.format(title,rating,regdate))
        self.con.commit()
    def updateRegdate(self,rating,regdate):
        sql="update webtoon set regdate='{}' where rating >={}"
        self.cur.execute(sql.format(regdate,rating))
        self.con.commit()
    def deleteRate(self,rating):
        sql="delete from webtoon where rating>={}"
        self.cur.execute(sql.format(rating))
        self.con.commit()
d1=DBManager()
# d1.insert('둘리','4.999','1990.01.01')
# d1.selectAll()
# d1.selectRating(9.9)
# d1.updateRegdate(9.9,'1999.03.05')
# d1.deleteRate(9.6)

color=['red','green','blue']
fruit=['apple','grape','peach','melon']
number=['one','two','three']
for c,f,n in zip(number,color,fruit):
    print(c,f,n)
