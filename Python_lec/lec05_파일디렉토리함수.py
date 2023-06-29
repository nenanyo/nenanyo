##----------------------------------------
## 파일 복사
## memo_utf8.txt파일을 memo_write.txt에 복사
##----------------------------------------

# fr = open(file="C:\\AI\\pythonProject\\venv\\test\\memo.utf8.txt", encoding= 'UTF-8', mode='r')
# fw = open(file="C:\\AI\\pythonProject\\venv\\test\\memo_write.txt", encoding= 'UTF-8',mode='a')
#
# txt_list = fr.readlines()
# for txt in txt_list:
#     fw.write(txt)
# fr.close()
# fw.close()
# print('==done==')

##------------------------------------------
from shutil import copy, copy2, copyfile
##------------------------------------------
# copy(원본파일, 타겟파일경로)
# copy(원본파일경로, 타켓파일경로)
# copy ("/etc/memo/a.txt", "/etc/memo2/b.txt")
# copy2("/etc/memo/a.txt", "/etc/memo2")  --> /etc/memo2/a.txt

orig = "C:\\AI\\pythonProject\\venv\\Python_basic\\memo.utf8.txt"
dest = "C:\\AI\\pythonProject\\venv\\Python_basic\\memo_write.txt"
copy(orig,dest)

##------------------------------------------
# 파일 & 디렉토리 내장 함수
# 절대경로(absolute path) : C:\\AI\\pythonProject\\venv\\Python_basic
# 상대경로(relative path) : 상대적으로 내가 위치한 폴더를 기준으로 경로
#      . 현재폴더  
#     .. 상위폴더
#      / 아래
##------------------------------------------


import  os
from os.path import isfile, isdir, join
##v: 변수/f: 함수/m: 매서드 내가 만든 것
print(os.getcwd())
print(os.listdir("C:\\AI\\pythonProject\\venv\\Python_basic"))
print(os.listdir(os.getcwd()))

pwd = os.getcwd()
print (pwd)

print("\n", "-"*80)

for f in os.listdir(pwd) :
    # print(os.getcwd()+"\\"+ f)
    print(join(os.getcwd(), f))

# print(join('/aa', 'bb.txt'))

print("\n", "-"*80)

path = join("C:\\AI\\pythonProject\\venv", f)
for f in os.listdir("C:\\AI\\pythonProject\\venv") :
    if os.path.isdir(path):
        print("[D]", path)
    elif os.path.isfile(path):
        print("\t\t",path)
print("---------------------------------------")
# from datetime import datetime
# strftime(datetime타입, "포맷")
##-- import한 이후에는 매써드 바로 사용
#datetime.datetime.strftime() -- import하지 않고 빌려쓰기

###-------------------수정날짜 구하기
import datetime as dt
float_mm = os.path.getmtime("C:\\Setup.log")
# print(type(float_mm), float_mm)
time_mm = dt.datetime.fromtimestamp(float_mm)
# print(type(time_mm),time_mm)
str_mm = dt.datetime.strftime(time_mm, "%Y-%m-%d %H-%M-%S")
# print(type(str_mm),str_mm)
###-------------------
print("\n", "-"*80)
for f in os.listdir("C:\\") :
    path = join("C:\\" ,f)
    float_mm = os.path.getmtime("C:\\Setup.log")
    time_mm = dt.datetime.fromtimestamp(float_mm)
    str_mm = dt.datetime.strftime(time_mm, "%Y-%m-%d %H-%M-%S")

    if os.path.isdir(path):
        print(f, "\t\t\t", "파일폴더", "\t\t", str_mm)
    elif os.path.isfile(path):
        fsize = os.path.getsize(path)
        print(f, "\t\t\t", "텍스트문서", "\t\t", str_mm, "\t\t", fsize/1024,"KB")
    if os.path.isdir(path):
        print("[D]", path)
    elif os.path.isfile(path):
        print("\t\t",path)
print("\n", "-"*80)

##----------------------------glob.py
# /etc/*.txt
# /etc/*c/a*.log -- like연산 같음
##----------------------------
import datetime as dt
import glob

print(glob.glob("C:\\P*"))
## p로 시작하는 어떤 거
print("---------------------------------------")
print(glob.glob("C:\\P*\\M*"))
print("---------------------------------------")
print(glob.glob("C:\\AI\\pythonProject\\venv\\Python_basic\\*.py"))
print("---------------------------------------")
module_list = glob.glob("C:\\AI\\pythonProject\\venv\\Python_basic\\lec*.py")
print(module_list)
print("---------------------------------------")
glist =glob.glob("C:\\AI\\pythonProject\\venv\\Python_basic\\*.py")
module_list =[]
for f in glist:
    print(os.path.split(f))
    module_list.append(f)
print("---------------------------------------")
for f in glist:
    f.split("\\")[-1]
    module_list.append(f.split("\\")[-1])


