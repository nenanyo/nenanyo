# pip install cx-Oracle
import os
import cx_Oracle
from os.path import isfile, isdir, join

def addr_insert(prm_name, prm_tel) :
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "insert into ADDR(seq, name, tel) values(ADDR_seq.nextval, :1, :2)"
    cur = conn.cursor()
    cur.execute(sql, [insertnm, inserttel])
    conn.commit()
    cur.close()
    conn.close()

def addr_update(prm_name, prm_tel, prm_seq) :
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "update ADDR set name=:1, tel=:2 where seq=:3"
    cur = conn.cursor()
    cur.execute(sql, [updatenm, updatetel, updateseq])
    conn.commit()
    cur.close()
    conn.close()

def addr_delete(prm_seq):
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "delete from addr where seq = :1"
    cur = conn.cursor()
    cur.execute(sql, [delete])
    conn.commit()
    cur.close()
    conn.close()

def addr_select():
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "select * from ADDR"
    cur = conn.cursor()
    cur.execute(sql)
    for row in cur:
        print( list(row)  )
    cur.close()
    conn.close()


def DB_save(fname):
    fr = open(file= fname, encoding='UTF-8', mode='r')
    txt_list = fr.readlines()
    data_list = []
    data_key1 = ""
    data_key2 = ""
    for i, txt in enumerate(txt_list):
        ltxt = txt.strip().split('*')
        if i == 0:
            data_key1 = ltxt[0]
            data_key2 = ltxt[1]
        else:
            data_list2 = {data_key1: ltxt[0], data_key2: ltxt[1]}
            print(data_list2)
            data_list.append(data_list2)
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "insert into ADDR(seq, name, tel) values(ADDR_seq.nextval, :name, :tel)"
    cur = conn.cursor()
    cur.executemany(sql, data_list)
    conn.commit()
    cur.close()
    conn.close()




def menu_print():
    print("------------------------------------------------")
    print("1.입력(insert)", end="\t")  # -----
    print("2.전체(select)", end="\t")  # -----
    print("3.삭제(delete)", end="\t")  # -----
    print("4.수정(update)", end="\t")  # -----
    print("5.파일저장", end="\t")  # -----
    print("6.종료")            # -----
    print("------------------------------------------------")


def run():
    while(True):
        menu_print()
        menu_input = input("명령어 입력: ")
        if menu_input=="6":
            break
        elif menu_input=="1":
            insertnm= input("name : ")
            inserttel = input("tel : ")
            addr_insert(insertnm, inserttel)
        elif menu_input == "2":
            addr_select()
        elif menu_input == "3":
            delete = input("seq: ")
            addr_delete(delete)
        elif menu_input == "4":
            updatenm = input("name : ")
            updatetel = input("tel : ")
            updateseq= input("seq : ")
            addr_update(updatenm, updatetel, updateseq)
        elif menu_input == "5":
            fname = input("대상파일명 : ")
            fullname = join(os.getcwd(), fname)
            if isfile(fullname):
                DB_save(fname)
            else:
                print("대상파일이 없습니다 확인 후 시도하세요")

if __name__ == "__main__" :
    print("직접돌려보기")
    run()
# #
# # --------------------------------------------------
# # insert : multi rows
# # --------------------------------------------------
# datas = [  {"vnm":"나이름1", "vtel":"111"} ,
#            {"vnm":"나이름2", "vtel":"222"} ,
#            {"vnm":"나이름3", "vtel":"333"}
#         ]
#

