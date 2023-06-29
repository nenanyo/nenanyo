##DFS : distributed file server, 분산파일서버, (HBASE, MONGE), NO-SQL, 빅데이터 처리
#\n : 줄바꿈
##--------------------------------
#open(파일경로, 모드) -- 반드시 close()해줘야함
##--------------------------------
#모드 : r(읽기), w(쓰기), a(추가)
# 리눅스&유닉스 (슬러시): /etc/guest/aa.txt
# 윈도우      (역슬러시): c:\aaa\bb.txt
# 파이썬 프로그래밍     : c:\\aaa\\bb.txt OR c:/aaa/bb.txt -- \ 하나는 end 뒤로 이해

f = open(file="C:\\AI\\pythonProject\\venv\\Python_basic\\memo.ansi.txt", mode='r')
f.close()


##--------------------------------
##읽기
#readline() : 라인 1줄
#readlines() : 전체 -- 리스트로 반환
#read(전체)  : 전체 -- 문서로 반환
# ANSI ASCII
# CP949 UTF-8
##--------------------------------

f = open(file="C:\\AI\\pythonProject\\venv\\Python_basic\\memo.ansi.txt", mode='r')
txt =  f.readline()
print(txt)
f.close()


f = open(file="C:\\AI\\pythonProject\\venv\\Python_basic\\memo.utf8.txt", encoding= 'UTF-8', mode='r')
while(True):
    txt =  f.readline()
    if not txt:
        break
    print(txt, end='')
f.close()
print('\n','-' * 80)

print(1)
print(bool(1))
print(bool(0))
print(True)

# while(1):  ----- true 일때 ,캐스팅(형변환)문법
#     print('0')

print('\n','-' * 80)

f = open(file="C:\\AI\\pythonProject\\venv\\Python_basic\\memo.utf8.txt", encoding= 'UTF-8', mode='r')
txts = f.readlines()
print(txts)
f.close()
### ['동해물과 \n', '백두산이\n', '마르고 닳도록']


for n in txts :
#    n = n.strip() #공백과 개행 제거
    print(n, end='')

print('\n','-' * 80)

f = open(file="C:\\AI\\pythonProject\\venv\\Python_basic\\memo.utf8.txt"
         , encoding= 'UTF-8'
         , mode='r')
txts = f.read()
print(txts)
f.close()

##--------------------------------
## with open() as f : 자동으로 close()해준다 --춫천
##--------------------------------

print('\n','-' * 80)

with open(file="C:\\AI\\pythonProject\\venv\\Python_basic\\memo.utf8.txt"
         , encoding= 'UTF-8'
         , mode='r') as f :
    txts = f.read()
    print(txts)

##--------------------------------
## 파일 쓰기
## with open(file = "파일경로', mode = 'w') as f :
##--------------------------------

with open(file="C:\\AI\\pythonProject\\venv\\Python_basic\\memo_write.txt",mode='w') as f:
    for num in range(1,11):
        f.write(str(num)+"\n")
print("=done=")

print('\n','-' * 80)
##----------------------------------------
## 파일 복사
## memo_utf8.txt파일을 memo_write.txt에 복사
##----------------------------------------
fr = open(file="C:\\AI\\pythonProject\\venv\\Python_basic\\memo.utf8.txt", encoding= 'UTF-8', mode='r')
fw = open(file="C:\\AI\\pythonProject\\venv\\Python_basic\\memo_write.txt", encoding= 'UTF-8',mode='a')
### 이미지, 동영상 copy는 mode='rb,rw'

txt_list = fr.readlines()
for txt in txt_list:
    fw.write(txt)
fr.close()
fw.close()








##----------------------------------------
