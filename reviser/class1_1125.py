import cx_Oracle
class DBManager:
    def __init__(self):
        self.con=cx_Oracle.connect('happy/day@localhost:1521/xe')
        self.cur=self.con.cursor()
        print('연결성공')
    def __del__(self):
        self.con.close()
        print('연결해제')
    def selectAll(self):
        sql='select * from webtoon order by no'
        self.cur.execute(sql)
        rows=self.cur.fetchall()
        for row in rows:
            print(row)

d1=DBManager()
d1.selectAll()