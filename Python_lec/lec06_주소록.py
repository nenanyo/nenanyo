addr_list = [{"name":"홍길동", "tel": "010"},
             {"name":"아무개", "tel": "111"},
            {"name":"홍길동", "tel": "555"}
             ]

def menu_print():
    print("-" * 80)
    print("1.입력",end="\t")
    print("2.조회",end="\t")
    print("3.전체",end="\t")
    print("4.삭제",end="\t")
    print("5.수정",end="\t")
    print("6.종료")
    print("-" * 80)


while(True) :
    menu_print()
    cmd = input("명령어입력 : ")
    print(cmd, type(cmd))
    if cmd =='6' :
        break
    elif cmd=="1":
        name = input("이름 : ")
        tel = input("전화번호 : ")
        addr_list.append({"name": name, "tel": tel})
    elif cmd=="3" :
        print(len(addr_list), "건")
        for addr_d in addr_list:
            print(addr_d["name"], "\t", addr_d["tel"])
    elif cmd=='2' :
        sname = input("검색이름 : ")
        slist = []
        for addr_d in addr_list:
            if addr_d["name"] ==sname:
                slist.append(addr_d["tel"])
        if len(slist) == 0 :
            print("검색 결과가 없습니다.")
        else :
            for stel in slist:
                print(stel)
    elif cmd=='4' :
        isdel = False
        dell = input("tel : ")
        for addr_d in addr_list:
            if addr_d["tel"] == dell:
                yn = input("정말 삭제하시겠습니까?(Y/N)")
                if yn.upper() =='Y':
                    addr_list.remove(addr_d)
                    isdel = True
        if isdel ==True:
            print("삭제완료")
        elif isdel == False:
            print("검색 결과가 없습니다.")
        print(addr_list)
    elif cmd=='5' :
        isupdate = False
        upd =input("tel : ")
        for addr_d in addr_list:
            if addr_d["tel"] == upd:
                ntel = input("new tel : ")
                addr_d["tel"] = ntel
                isupdate = True
        if isupdate ==True:
            print("수정완료")
        elif isupdate == False:
            print("검색 결과가 없습니다.")
        print(addr_list)


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