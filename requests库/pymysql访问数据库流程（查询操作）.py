import pymysql

conn = pymysql.connect('localhost', 'root', 'root', 'books')
cursor = conn.cursor()
sql = "select id,title,`read`,comment from t_book"
cursor.execute(sql)

for i in range(cursor.rowcount):
    print(cursor.fetchall())    # 游标会下移,limit start, offset,
    print(cursor.fetchone())

cursor.close()
conn.close()
