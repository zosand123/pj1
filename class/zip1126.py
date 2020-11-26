import cx_Oracle

class DBManager:
    # 오라클은 my.cursors.DictCursor같은 데이터를 dict으로 가져오는 함수가 없어서
    # 직접 만들어 써야한다.
    def makeDictFactory(self,cur):
        # for colinfo in self.cur.description:
        #     # print(culinfo)
        #     print(colinfo[0])
        colnames = [colinfo[0] for colinfo in self.cur.description]
        print(colnames)
        # print(cur.fetchall()) #[(),(),()]
        templist=[]
        for datas in cur.fetchall(): #datas=(),(),()
            temp = {}
            # print(datas)
            # print(colnames)
            for k,v in zip(colnames,datas):
                # print(k,v)
                temp[k]=v #k의 value는 v다
            # print(temp)
            templist.append(temp)
        return templist
        # def createRow():
        #     print('createRow()함수')
        # return createRow()


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
        result = self.makeDictFactory(self.cur)
        for row in result:
            print(row)
            print()
            print(row['NO'],row['TITLE'],row['RATING'],row['REGDATE'])

    def selectRating(self, rating):
        sql = "select * from webtoon where rating>={}"
        self.cur.execute(sql.format(rating))
        result = self.makeDictFactory(self.cur)
        for row in result:
            # print(row)
            # print()
            print(row['NO'], row['TITLE'], row['RATING'], row['REGDATE'])
d1=DBManager()
# d1.selectAll()
d1.selectRating(6.6)
# color=['red','green','blue']
# fruit=['apple','grape','peach','melon']
# number=['one','two','three']
# for c,f,n in zip(number,color,fruit):
#     print(c,f,n)
