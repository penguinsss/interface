"""
事务提交机制：
    自动提交：
        1 建立连接设置autocommit=True来设置自动提交
        2 建立连接后，通过conn.autocommit(True)来设置
    手动提交：
        1 conn.rollback 进行回滚
        2 conn.commit 进行提交

"""

import pymysql

conn, cursor = None, None
try:
    conn = pymysql.connect('localhost', 'root', 'root', 'books')  # utf8, utf-8不行
    cursor = conn.cursor()

    insert_book_sql = "insert into t_book(title, pub_date) values ('精英律师','2019-12-24')"
    insert_hero_sql = "insert into t_hero(`name`, `gender`, `book_id`) values('ww', 1, 11)"

    # 操作
    cursor.execute(insert_book_sql)
    cursor.execute(insert_hero_sql)

    # 🎈 只是先存到了内存中，并没有持久化
    cursor.execute("select * from t_book")
    print(cursor.fetchall())
    cursor.execute("select * from t_hero")
    print(cursor.fetchall())

    # 如果自动提交事务没有开启，那么需要手动提交事务，否则在代码中的操作不会真正的把数据提交到数据库
    conn.commit()
except Exception as e:
    conn.rollback()
    print('已触发回滚操作！')
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
