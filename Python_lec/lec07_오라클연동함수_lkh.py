# pip install cx-Oracle
import os

import cx_Oracle
from os.path import isfile, join

def addr_insert(prm_name, prm_tel) :
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :1, :2)"
    cur = conn.cursor()
    cur.execute(sql, [prm_name, prm_tel])
    conn.commit()
    cur.close()
    conn.close()

def addr_select():
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "select * from addr"
    cur = conn.cursor()
    cur.execute(sql)
    for row in cur:
        print( list(row)  )
    cur.close()
    conn.close()

def addr_update(prm_name, prm_tel, prm_seq) :
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "update addr set name=:1, tel=:2 where seq=:3"
    cur = conn.cursor()
    cur.execute(sql, [prm_name, prm_tel, prm_seq])
    conn.commit()
    cur.close()
    conn.close()

def addr_delete(prm_seq):
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "delete from addr where seq = :1"
    cur = conn.cursor()
    cur.execute(sql, [prm_seq])
    conn.commit()
    cur.close()
    conn.close()


def menu_print():
    print("------------------------------------------------")
    print("1.입력(insert)", end="\t")  # -----
    print("2.전체(select)", end="\t")  # -----
    print("3.수정(update)", end="\t")  # -----
    print("4.삭제(delete)", end="\t")  # -----
    print("5.파일저장", end="\t")            # -----
    print("6.종료")  # -----
    print("------------------------------------------------")

def file_db_insert(fname) :
    fr = open(file=fname, encoding='UTF-8', mode='r')
    txt_list = fr.readlines()
    data_list = []
    dict_key1 = ""
    dict_key2 = ""
    for i, txt in enumerate(txt_list):
        tlist = txt.strip().split("*")
        if len(tlist) != 2:
            print("__*__ 형식의 포맷이 아닙니다")
            break
        if i == 0:
            dict_key1 = tlist[0]
            dict_key2 = tlist[1]
        else:
            data_dict = {dict_key1: tlist[0], dict_key2: tlist[1]}
            print(data_dict)
            data_list.append(data_dict)
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :name, :tel)"
    cur = conn.cursor()
    cur.executemany(sql, data_list)
    conn.commit()
    cur.close()
    conn.close()

    # datas = [  {"name":"나이름1", "tel":"111"} ,
    #            {"name":"나이름2", "tel":"222"} ,
    #            {"name":"나이름3", "tel":"333"}
    #         ]




def run() :
    while (True):
        menu_print()  # -----------------------------------------
        cmd = input("명령어입력:")
        if cmd == "1":
            nm = input("이름:")
            tel = input("전화번호:")
            addr_insert(nm,tel)  # -----------------------------------------
        elif cmd == "2":
            addr_select()
        elif cmd == "3":
            nm = input("이름:")
            tel = input("전화번호:")
            seq = input("번호:")
            addr_update(nm,tel, seq)
        elif cmd == "4":
            seq = input("번호:")
            addr_delete(seq)  # -----------------------------------------
        elif cmd == "5":
            fname = input("대상파일명:")
            # if len(fname) == 0:
            #     fname = "lec06_주소록.txt"
            fullname = join(os.getcwd() , fname)
            if isfile(fullname) :
                file_db_insert(fname)
            else :
                print("대상파일이 없습니다 확인 후 시도하세요")
        elif cmd == "6":
            break

if __name__ == "__main__" :
    print("직접돌려보기")
    run()



