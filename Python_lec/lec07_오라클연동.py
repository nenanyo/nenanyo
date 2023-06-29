###--------WHEEL(whl) : 파이썬 압축파일
##-- pip install cx-oracle

import cx_Oracle
##sql문 점검 후에 해보기

# with  cx_Oracle.connect("ai","0000","localhost:1521/XE") as conn :
#     if bool(conn):
#     ##---conn =1
#         print("연결성공")
#     else:
#         print("연결실패")
#     with conn.cursor() as cur:
#         cur.execute("select * from emp")
#         for c in cur:
#             print(list(c))
### 열고 닫기 귀찮으니까 with 이용


##-----------------------------------------------
##연결 & 닫기
##-----------------------------------------------

# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# if bool(conn):
# ##---conn =1
#     print("연결성공")
# else:
#     print("연결실패")
# conn.close()

##-----------------------------------------------
## insert : 1 row
## INSERT INTO ADDR VALUES(ADDR_SEQ.NEXTVAL, '홍길동', '000');
##-----------------------------------------------
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "INSERT INTO ADDR(seq,name,tel) VALUES(ADDR_SEQ.NEXTVAL, :1, :2)"
# ## ;는 있으면 안 된다
# cur = conn.cursor()
# cur.execute(sql,['아무개','555'])
# cur.execute(sql,['김김김','2525'])
# conn.commit()
# cur.close()
# conn.close()
#

# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# ##sql = "INSERT INTO ADDR(seq,name,tel) VALUES(ADDR_SEQ.NEXTVAL, :1, :2)"
# sql = "INSERT INTO ADDR(seq,name,tel) VALUES(ADDR_SEQ.NEXTVAL, :vnm, :vtel)"
# ##변수는 맘대로
# ## ;는 있으면 안 된다
# cur = conn.cursor()
# cur.execute(sql,{'vnm':'아무개2','vtel':'555'})
# conn.commit()
# cur.close()
# conn.close()

##-----------------------------------------------
## insert : multi rows
##-----------------------------------------------

# datas = [{'vnm':'아무개3','vtel':'666'}
#         ,{'vnm':'아무개4','vtel':'777'}
#         ,{'vnm':'아무개5','vtel':'888'}
#         ,{'vnm':'아무개6','vtel':'999'}
#          ]
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "INSERT INTO ADDR(seq,name,tel) VALUES(ADDR_SEQ.NEXTVAL, :vnm, :vtel)"
# ##변수는 맘대로
# ## ;는 있으면 안 된다
# cur = conn.cursor()
# cur.executemany(sql,datas)
# conn.commit()
# cur.close()
# conn.close()


# datas = [["리스트1","123"]
#         ,["리스트2","123"]
#         ,["리스트3","123"]
#          ]
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "INSERT INTO ADDR(seq,name,tel) VALUES(ADDR_SEQ.NEXTVAL, :1, :2)"
# cur = conn.cursor()
# cur.executemany(sql,datas)
# conn.commit()
# cur.close()
# conn.close()

##-----------------------------------------------
## update
## update ADDR set name = '홍길순', tel = '999' where seq = 1
##-----------------------------------------------

conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
sql = "update ADDR set name=:1, tel=:2 where seq=:3"
cur = conn.cursor()
cur.execute(sql, ['홍길순', '999', 1])
conn.commit()
cur.close()
conn.close()

##-----------------------------------------------
## delete
## delete from ADDR where name like '%나이름%' or name like '%리스트%';
##-----------------------------------------------
# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "delete from ADDR where name like :1 or name like :2"
# cur = conn.cursor()
# cur.execute(sql,['%나이름%','%리스트%'])
# conn.commit()
# cur.close()
# conn.close()


##-----------------------------------------------
## select
##-----------------------------------------------
conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
cur = conn.cursor()
cur.execute("select * from ADDR")
for c in cur:
    print(list(c))
cur.close()
conn.close()

# conn = cx_Oracle.connect("ai","0000","localhost:1521/XE")
# sql = "select * from ADDR where seq = :1"
# cur = conn.cursor()
# cur.execute(sql,[12,])
# for c in cur:
#     print( list(c) )
# cur.close()
# conn.close()
