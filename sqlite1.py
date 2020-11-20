#sqlite-tools-win32-x86-3330000.zip #압축해제해서 D:\sqlite 에 둔다
#sqlite3 #파이썬에서 제공하는 db, 가벼움
#.open 데이터베이스이름
#.open pythonDB - 없으면 만들어준다
#.table : 현재데이터베이스 테이블목록
# create table member(
#     id char(4),
#     name char(20),
#     age int,
#     email char(30),
#     birthyear int);
# .table
# .schema 테이블이름 : 테이블의 구조확인
# insert into member values ('aaa','Kim','33','aa@naver.com','2010');
# insert into member values ('bbb','Lee','13','bb@naver.com','2001');
# select * from member;
# .header on #select 사용시 컬럼명보이기
# .mode column # select 사용시 컬럼모드로 줄맞춰보이기
# select * from member;
# .quit  #빠져나가기
# --------
# sqlite3
# .open pythondb
# .table
# import sqlite3
# # 1) 데이터베이스연결
# con=sqlite3.connect("d:\\sqlite\\pythonDB")
# # 2) 커서 생성
# cur=con.cursor()
# # 3) 쿼리생성
# sql="select * from member"
# # 4) 실행 및 처리
# cur.execute(sql)
# while(True):
#     row=cur.fetchone()
#     if row==None:
#         break
#     print(row[0],row[1],row[2],row[3])
# # 5) 자원해제
# con.close()

#----------------------------------------------------
import sqlite3
# 1) 데이터베이스연결
con=sqlite3.connect("d:\\sqlite\\pythonDB")
# 2) 커서 생성
cur=con.cursor()
while(True):
    id=input('사용자id=')
    if id=="":
        break
    name=input('사용자이름=')
    age=input('사용자나이=')
    email=input('사용자이메일=')
    birthyear=input('사용자 태어난 년도=')

    # 3) 쿼리생성
    sql="insert into member values('"+id+"','"+name+"',"+age+",'"+email+"',"+birthyear+")"
    # 4) 실행 및 처리
    cur.execute(sql)
con.commit()
# 5) 자원해제
con.close()

#삭제 ----
# # 1) 데이터베이스연결
# con=sqlite3.connect("d:\\sqlite\\pythonDB")
# # 2) 커서 생성
# cur=con.cursor()
# # 3) 쿼리생성
# sql="delete from member"
# # 4) 실행 및 처리
# cur.execute(sql)
# con.commit
# # 5) 자원해제
# con.close()