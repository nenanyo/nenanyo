#
addr_list = [ {"name":"홍길동",  "tel":"010"},
              {"name":"홍길동",  "tel":"555"},
              {"name":"아무개",  "tel":"111"}
            ]

def addr_file_write():
    with open(file="./lec06_주소록.txt", mode="w", encoding="UTF-8") as fw:
        fw.write("name  tel\n")
        for addr_dic in addr_list:
            temp = addr_dic["name"]+"\t"+addr_dic["tel"]+"\n"
            fw.write(temp)


def menu_print():
    print("------------------------------------------------")
    print("1.입력", end="\t")  # -----
    print("2.검색", end="\t")  # -----
    print("3.전체", end="\t")  # -----
    print("4.삭제", end="\t")  # -----
    print("5.수정", end="\t")  # -----
    print("6.종료")            # -----
    print("------------------------------------------------")

def addr_input():
    name = input("이름:")
    tel = input("전화번호:")
    addr_list.append({"name": name, "tel": tel})

def addr_search_all():
    print("총", len(addr_list), "건")
    for addr_dic in addr_list:
        print(addr_dic["name"], "\t", addr_dic["tel"])

def addr_search() :
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

def addr_delete():
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

def addr_update():
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

def run() :
    while (True):
        menu_print()  # -----------------------------------------
        cmd = input("명령어입력:")
        if cmd == "1":
            addr_input()  # -----------------------------------------
            addr_file_write()
        elif cmd == "2":
            addr_search()  # -----------------------------------------
        elif cmd == "3":
            addr_search_all()  # -----------------------------------------
        elif cmd == "4":
            addr_delete()  # -----------------------------------------
            addr_file_write()
        elif cmd == "5":
            addr_update()  # -----------------------------------------
            addr_file_write()
        elif cmd == "6":
            break

if __name__ == "__main__" :
    print("직접돌려보기")
    run()