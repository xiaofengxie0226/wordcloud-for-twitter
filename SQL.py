import psycopg2

conn = psycopg2.connect(dbname="tsetdb", user="postgres",
        password="password", host="127.0.0.1", port="5432")

cur = conn.cursor()
cur.execute(
        'CREATE TABLE test_user ('
        'ID SERIAL primary key,'#主键自动生成
        'name    varchar(80),'
        'date    date'
        ')'
    )

cur.execute("INSERT INTO test_user (name,mailaddress,date)"#插入需要指定
        "VALUES('sayama', 'sayama@gmail.com', '2020-04-18')")

cur.execute("SELECT * FROM test_user")
rows = cur.fetchall()
for row in rows:
    print(type(row))

conn.commit()
conn.close()
