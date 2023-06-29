# for 조건식 :
#   반복실행문
# while(조건식) :
#   반복실행문
# do: -------------파이썬은 없다
#     반복실행문
# while(조건식)
##------------------------------------------
emp = [7788,7799,7800]
##empno = emp[0] ---- 반복

for empno in emp:
    print(empno)
##--------------------------------------------    
##range(시작번호[이상],끝번호[미만*],증감분)
##--------------------------------------------
print(range(1,6,1))
print(list(range(1,6,1)))
##range라는 객체이다, 내용물을 볼려면 list
##증감분 기본 1, 안쓰면 1 적용
print(list(range(1,11)))
## 10까지
print(list(range(10,0,-1)))
## 10~1까지

for A in range(1,11) :
    print (A, end=" ")
print()
## print (A, end="\t") - tab
## print (A, end="\,") - ,

nums = [1,2,3,4,5,6,7,8,9,10]
for A in nums:
    print (A, end=' ')
print()
## --줄바꿈


##----------------------- 중첩 for문(들여쓰기가 중요하다)
for B in range(100,600,100):
    print(B)
    for C in range(1,4) :
        print(C, end="\t")
    print()
##----------------------- 구구단
dan = 2
gob = 3
print(dan,'*', gob, '=', dan*gob)

for dan in range(2,10) :
    print()
    print(dan, '단')
    for gob in range(1,10) :
        print(dan,'*', gob, '=', dan*gob, end='\t')

print()
for dan in range(2,10,2) :
    print(dan, '단')
    for gob in range(1,6) :
        print(dan,'*', gob, '=', dan*gob, end='\t')
        print()

print()
for dan in range(9,2,-2) :
    print(dan, '단')
    for gob in range(9,4,-1) :
        print(dan,'*', gob, '=', dan*gob, end='\t')
    print()
##-----------------------
#   *
#  ***
# *****

for i in range(3):
    print(' ' * (2-i), end='')
    print((i * 2 + 1) * '*')

for i in range(1,5):
    print('-'*(i-1), end = '')
    print((5-i)*'*', end = '')
    print()


for j in range(1,5):
    for k in range(1,5):
        if j<= k :
            print('*', end = '')
        else :
            print('-', end = '')
    print()


for i in range(1,5):
    print('*'*(i-1), end = '')
    print((5-i)*'-', end = '')
    print()

for i in range(1,5):
    print('-'*(4-i), end = '')
    print((i)*'*', end = '')
    print()

for j in range(1,5):
    for k in range(4,0,-1):
        if j< k :
            print(' ', end = '')
        else :
            print('*', end = '')
    print()

