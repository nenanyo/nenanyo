# pip install cx-Oracle

import cx_Oracle

# with cx_Oracle.connect("ai", "0000", "localhost:1521/XE") as conn :
#     if bool(conn) :
#         print("연결성공")
#     else:
#         print("연결실패")
#     with conn.cursor() as cur:
#         cur.execute("select * from emp")
#         for row in cur:
#             print( list(row)  )
#         # cur.close()
# # conn.close()


#--------------------------------------------------
# DDL & DML
#--------------------------------------------------
# CREATE TABLE ADDR (
#     SEQ number PRIMARY KEY ,
#     NAME VARCHAR2(10),
#     TEL VARCHAR2(15)
# );
#
# drop sequence addr_seq ;
# create sequence addr_seq
# start with 1
# increment by 1
# nocache;
#
# insert into addr values(addr_seq.nextval, '홍길동', '000');
# select * from addr;
# commit;
# #--------------------------------------------------


#--------------------------------------------------
# 연결 & 닫기
#--------------------------------------------------
conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
if bool(conn) :
    print("연결성공")
else:
    print("연결실패")
conn.close()

#--------------------------------------------------
# insert : 1 row
# insert into addr values(addr_seq.nextval, '홍길동', '000');
#--------------------------------------------------
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :1, :2)"
# cur = conn.cursor()
# cur.execute(sql, ['아무개', '555'])
# cur.execute(sql, ['함소영', '2525'])
# conn.commit()
# cur.close()
# conn.close()

# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :vnm, :vtel)"
# cur = conn.cursor()
# vnm = "나변수"
# vtel= "999"
# cur.execute(sql, [vnm, vtel])
# conn.commit()
# cur.close()
# conn.close()

# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :vnm, :vtel)"
# cur = conn.cursor()
# cur.execute(sql, {"vnm":"나변수2", "vtel":"8989"})
# conn.commit()
# cur.close()
# conn.close()



#--------------------------------------------------
# insert : multi rows
#--------------------------------------------------
# datas = [  {"vnm":"나이름1", "vtel":"111"} ,
#            {"vnm":"나이름2", "vtel":"222"} ,
#            {"vnm":"나이름3", "vtel":"333"}
#         ]
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :vnm, :vtel)"
# cur = conn.cursor()
# cur.executemany(sql, datas)
# conn.commit()
# cur.close()
# conn.close()


# datas = [  ["리스트1","6666"],
#            ["리스트2","8888"],
#            ["리스트3","9999"]
#         ]
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :1, :2)"
# cur = conn.cursor()
# cur.executemany(sql, datas)
# conn.commit()
# cur.close()
# conn.close()



#--------------------------------------------------
# update
# update addr set name='홍길순', tel='999' where seq=1
#--------------------------------------------------
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "update addr set name=:1, tel=:2 where seq=:3"
# cur = conn.cursor()
# cur.execute(sql, ['홍길순', '999', 1])
# conn.commit()
# cur.close()
# conn.close()



#--------------------------------------------------
# delete
# delete from addr where name like '%나이름%' or name like '%리스트%'
#--------------------------------------------------
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "delete from addr where name like :1 or name like :2"
# cur = conn.cursor()
# cur.execute(sql, ['%나이름%', '%리스트%'])
# conn.commit()
# cur.close()
# conn.close()


#--------------------------------------------------
# select
#--------------------------------------------------
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "select * from addr"
# cur = conn.cursor()
# cur.execute(sql)
# for row in cur:
#     print( list(row)  )
# cur.close()
# conn.close()


conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
sql = "select * from addr where seq = :1 or seq = :2"
cur = conn.cursor()
cur.execute(sql, [5, 1])
for row in cur:
    print( list(row)  )
cur.close()
conn.close()


