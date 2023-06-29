
def menu_print():
    print("------------------------------------------------")
    print("1.입력", end="\t")  # -----
    print("2.검색", end="\t")  # -----
    print("3.전체", end="\t")  # -----
    print("4.삭제", end="\t")  # -----
    print("5.수정", end="\t")  # -----
    print("6.종료")            # -----
    print("------------------------------------------------")

addr_list = [ {"name":"홍길동",  "tel":"010"},
              {"name":"홍길동",  "tel":"555"},
              {"name":"아무개",  "tel":"111"}
            ]
while(True) :
    menu_print()
    cmd = input("명령어입력:")
    if cmd == "6":
        break
    elif cmd == "1":
        name = input("이름:")
        tel  = input("전화번호:")
        addr_list.append({"name": name, "tel": tel})
    elif cmd == "3":
        print( "총", len(addr_list) , "건" )
        for addr_dic in addr_list:
            print(addr_dic["name"], "\t", addr_dic["tel"])
    elif cmd == "2":
        search_name = input("검색이름:")
        search_list = []
        for addr_dic in addr_list:
            if addr_dic["name"] == search_name:
                search_list.append(addr_dic["tel"])

        if len(search_list) == 0:
            print("검색 결과가 없습니다")
        else:
            for search_tel in search_list:
                print(search_tel)
    elif cmd == "4":
        isdel = False
        search_tel = input("삭제 전화번호:")
        for i, addr_dic in enumerate(addr_list):
            if addr_dic["tel"] == search_tel:
                yn = input("정말 삭제하시겠습니까?(Y/N)")
                if yn.upper() == "Y":
                    # del addr_list[i]
                    addr_list.pop(i)
                    isdel = True
        if isdel == True:
            print("삭제되었습니다")
        elif isdel == False:
            print("검색 결과가 없습니다")

        # for addr_dic in addr_list:
        #     if addr_dic["tel"] == search_tel:
        #         addr_list.remove(addr_dic)

    elif cmd == "5":
        isupdate = False
        search_tel = input("수정 전화번호:")
        for addr_dic in addr_list:
            if addr_dic["tel"] == search_tel:
                update_tel = input("변경할 전화번호:")
                addr_dic["tel"] = update_tel
                isupdate = True
        if isupdate == True:
            print("수정되었습니다")
        elif isupdate == False:
            print("검색 결과가 없습니다")


