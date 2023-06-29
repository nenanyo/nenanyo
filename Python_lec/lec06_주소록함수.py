addr_list = [{"name":"홍길동", "tel": "010"},
             {"name":"아무개", "tel": "111"},
            {"name":"홍길동", "tel": "555"}
             ]


def addr_file_write():
    with open(file="./lec06_주소록.txt", mode="w", encoding="UTF-8") as fw:
        fw.write("name  tel\n")
        for addr_dic in addr_list:
            temp = addr_dic["name"]+"\t"+addr_dic["tel"]+"\n"
            fw.write(temp)


def menu_print():
    print("-" * 80)
    print("1.입력",end="\t")
    print("2.조회",end="\t")
    print("3.전체",end="\t")
    print("4.삭제",end="\t")
    print("5.수정",end="\t")
    print("6.종료")
    print("-" * 80)

def addr_input():
    name = input("이름 : ")
    tel = input("전화번호 : ")
    addr_list.append({"name": name, "tel": tel})

def addr_searchall():
    print(len(addr_list), "건")
    for addr_d in addr_list:
        print(addr_d["name"], "\t", addr_d["tel"])

def addr_search():
    sname = input("검색이름 : ")
    slist = []
    for addr_d in addr_list:
        if addr_d["name"] == sname:
            slist.append(addr_d["tel"])
    if len(slist) == 0:
        print("검색 결과가 없습니다.")
    else:
        for stel in slist:
            print(stel)

def addr_del():
    isdel = False
    dell = input("tel : ")
    for addr_d in addr_list:
        if addr_d["tel"] == dell:
            yn = input("정말 삭제하시겠습니까?(Y/N)")
            if yn.upper() == 'Y':
                addr_list.remove(addr_d)
                isdel = True
    if isdel == True:
        print("삭제완료")
    elif isdel == False:
        print("검색 결과가 없습니다.")
    print(addr_list)

def addr_update():
    isupdate = False
    upd = input("tel : ")
    for addr_d in addr_list:
        if addr_d["tel"] == upd:
            ntel = input("new tel : ")
            addr_d["tel"] = ntel
            isupdate = True
    if isupdate == True:
        print("수정완료")
    elif isupdate == False:
        print("검색 결과가 없습니다.")
    print(addr_list)
##-------------------------------------------------------------------------
def run():
    while(True) :
        menu_print()
        cmd = input("명령어입력 : ")
        print(cmd, type(cmd))
        if cmd =='6' :
            break
        elif cmd=="1":
            addr_input()
            addr_file_write()
        elif cmd=="3" :
            addr_searchall()
        elif cmd=='2' :
            addr_search()
        elif cmd=='4' :
            addr_del()
            addr_file_write()
        elif cmd=='5' :
            addr_update()
            addr_file_write()

if __name__ =="__main__":
    print("직접")
    run()





# addr_list = []
# addr_list.append(1)
# addr_list.append({"name": "홍길동", "tel" :" 032"})
# addr_list.append([3,3,{"name": "홍길동"}])
# print(addr_list[1]["name"])













# A = [1,2,3,'AA',5,{"name":"홍길동", "tel": "010"}]
#
# for n, val in enumerate(A) :
#     print(n, val)
#     if val == 'AA':
#         del A[n]
# print (A)


## ----숫자 세기 함수 :
# for n, val in enumerate(A) :
#     print(n, val)