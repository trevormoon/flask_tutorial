import mysql.connector as my

try:
    conn=my.connect(host="127.0.0.1",user="root",passwd="1234",database="world")
    cur=conn.cursor()

    sql="insert into student values('이순신',30,'1994-04-05')"
    cur.execute(sql)
    conn.commit()
    conn.close()
except Exception as err:
    print("에러문 :",err)