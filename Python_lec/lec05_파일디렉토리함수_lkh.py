# # --------------------------
# # 파일 복사(copy)
# # memo_utf8.txt 파일을 memo_write.txt에 복사
# # --------------------------
# fr = open(file="C:\\AI\\pythonProject\\venv\\python_basic\\memo_utf8.txt",  encoding='UTF-8', mode='r')
# fw = open(file="C:\\AI\\pythonProject\\venv\\python_basic\\memo_write.txt", encoding='UTF-8', mode='w')
# txt_list = fr.readlines()
# for txt in txt_list:
#     fw.write(txt)
# fr.close()
# fw.close()
# print("====copy done===")
# with open(file="C:\\AI\\pythonProject\\venv\\python_basic\\memo_write.txt"
#         , encoding='UTF-8', mode='r') as f:
#     print(f.read())

#-------------------------------------
from shutil import copy, copy2, copyfile
#-------------------------------------
# copy(원본파일경로, 타켓파일경로)
# copy ("/etc/memo/a.txt", "/etc/memo2/b.txt")
# copy2("/etc/memo/a.txt", "/etc/memo2")  --> /etc/memo2/a.txt

orig = "C:\\AI\\pythonProject\\venv\\python_basic\\memo.utf8.txt"
dest = "C:\\AI\\pythonProject\\venv\\python_basic\\memo_write.txt"
copyfile(orig, dest)


#-------------------------------------
# 파일&디렉토리 내장 함수
# 절대경로(Absolute Path) : C:\\AI\\pythonProject
# 상대경로(Relative Path) : 상대적으로 내가 위치한 폴더를 기준의 경로
#      .  현재폴더
#     ..  상위폴더
#      /  아래
#-------------------------------------
import os
from os.path import isfile, isdir, join
#
# print(os.getcwd())
# print(os.listdir("C:\\AI\\pythonProject\\venv\\python_basic"))
# print(os.listdir(os.getcwd()))
#
# pwd = os.getcwd()
# print(os.listdir(pwd))
#
# print("\n", "--"*40)
# # --------------------------------------------------
# for f in os.listdir(pwd) :
#     # print(os.getcwd() +  "\\" + f)
#     print(  join( os.getcwd() , f)  )
#
#
# print("\n", "--"*40)
# # --------------------------------------------------

# from 패키지/datetime.py import strftime()
# from datetime.datetime import strftime
# strftime(datetime타입,  "포맷")

import datetime as dt

float_mm = os.path.getmtime("C://Setup.log")   #1541654654.456464465
print( type(float_mm),   float_mm)

time_mm = dt.datetime.fromtimestamp(float_mm)
print( type(time_mm),   time_mm)

str_mm =  dt.datetime.strftime(time_mm,  "%Y-%m-%d %H:%M:%S")
print(  type(str_mm),  str_mm )



for f in os.listdir("C:\\") :
    path = join( "C:\\" , f)

    # ------------------------ 수정날짜 구하기 ---------------------
    float_mm = os.path.getmtime(path)  # 1541654654.456464465
    time_mm  = dt.datetime.fromtimestamp(float_mm)
    str_mm   = dt.datetime.strftime(time_mm, "%Y-%m-%d %H:%M:%S")
    #---------------------------------------------------------------
    if os.path.isdir(path) :
        print(f, "\t\t\t", "파일폴더", "\t\t", str_mm)
    elif os.path.isfile(path) :
        fsize = os.path.getsize(path)   #byte Kbyte
        print(f, "\t\t\t", "텍스트문서", "\t\t", str_mm, "\t\t", fsize/1024, "KB")

#------------------------------------------------------
# os.listdir()
# os.path.isdir()
# os.path.isfile()
# os.path.join()
#------------------------------------------------------ 번외
# for f in os.listdir("C:\\") :
#     path = join( "C:\\" , f)
#     if os.path.isdir(path) :
#         if f == "AI" :
#             subpath = join("C:\\", f)   #C:\\AI
#             for sf in os.listdir(subpath):
#                 fullname = join(subpath, sf)    #C:\\AI\\python38
#                 if os.path.isdir(fullname):
#                     print("------", sf)
#                 elif os.path.isfile(fullname):
#                     print("------", sf)
#         else :
#             print("[D]", f)
#     elif os.path.isfile(path) :
#         print("\t", f)


#-----------------------------------glob.py
#  /etc/*.txt
#  /etc/*c/a*.log
# -------------------------------------------
import glob

print(  glob.glob("C:\\P*") )

print(  glob.glob("C:\\P*\\M*") )
print(  glob.glob("C:\\AI\\pythonProject\\venv\\python_basic\\lec*.py")  )


print("----------------------")
glist = glob.glob("C:\\AI\\pythonProject\\venv\\python_basic\\lec*.py")
module_list = []
for fname_str in glist:
    module_list.append(  fname_str.split("\\")[-1]   )
    # print(os.path.split(fname_str))     #(경로, 파일명)
    # print(os.path.basename(fname_str))  #파일명
    # print(os.path.dirname(fname_str))   #경로
    # print(os.path.splitext(fname_str))  #( 경로/파일명 , .py(확장자) )
print( module_list )










