import cx_Oracle
con=cx_Oracle.connect('happy/day@localhost:1521/xe')
cur=con.cursor()
sql='delete from songs where no>10'
cur.execute(sql)
con.commit()
con.close()
