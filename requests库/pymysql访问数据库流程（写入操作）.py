# 通过pymysql完成操作mysql数据的本质：通过游标执行sql语句

import pymysql

# 写入（insert、update、delete）时需修改autocommit为True
conn = pymysql.connect('localhost', 'root', 'root', 'books')  # utf8, utf-8不行
cursor = conn.cursor()
# insert_sql = "insert into t_book(title, pub_date) values ('放羊的星星','1995-12-24'), ('放羊的星星1','1995-12-27')"
# print(cursor.execute(insert_sql))

# update_sql = "update t_book set `read` = `read` + 1 where title = '放羊的星星'"
# cursor.execute(update_sql)

# delete_sql = "delete from t_book where title = '放羊的星星'"
# cursor.execute(delete_sql)

print(cursor.execute("select * from t_book"))
cursor.close()
conn.close()

