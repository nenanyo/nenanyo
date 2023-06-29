## if 조건식 : 실행1
## else : 실행2
##----------------
## if 조건식 : 실행1
## elif 조건식: 실행2
## elif 조건식: 실행2
##----------------
## if 조건식 : 실행1
## elif 조건식: 실행2
## else : 실행3
##----------------
##if 단독으로도 가능,필수!!
##else는 옵션
##elif는 원하는 만큼

## 들여쓰기(indentation) 주의해서 하자
score = 80
if score >= 90 :
    print('A')
elif score >=80 :
    print('B')
else : 
    print('C')
##---------------------------------------
## "=" 는 정의 // "=="는 같다(비교)
score  = 80
gen = '남'
if score >= 90 :
    if gen=='남' :
        print('1')
    elif gen=='여':
        print('2')
elif score >= 80 :
    if gen=='남' :
        print('11')
    elif gen=='여':
        print('22')
else : print('0')

if score>=90 and gen =='남' :
    print('1')
elif score>=90 and gen =='여' :
    print('2')
elif score>=80 and gen =='남' :
    print('11')
elif score>=80 and gen =='여' :
    print('22')
else : print('0')
##---------------------------------------

