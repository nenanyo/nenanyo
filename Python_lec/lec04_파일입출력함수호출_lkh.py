#---------------------------------------------------------
# python_basic lec04_파일입출력함수_lkh.py  CalcClass add()
#---------------------------------------------------------
# 1. from   : 패키지명.모듈명
# 2. import : 클래스명, 모듈명, 함수명
# 3. 모듈명은 일반적으로 별칭(alias)를 사용한다
# 4. import 함수명1, 함수명2 이 길어지면 import 모듈명으로 한다
#
#       ex) from 패키지명.모듈명 import 클래스명
#       ex) from 패키지명.모듈명 import 함수명1, 함수명2 ...
#       ex) from 패키지명       import 모듈명 as 별명
#---------------------------------------------------------
from python_basic.lec04_파일입출력함수_lkh import CalcClass
from python_basic.lec04_파일입출력함수_lkh import MemberClass
from python_basic.lec04_파일입출력함수_lkh import myprint, uprint

a = CalcClass.add(1,5)
print(a)
print(CalcClass.add(1,5))

MemberClass.add("kim", 30)
myprint(5)
uprint(5)

#---------------------------------------------------------
from python_basic import lec04_파일입출력함수_lkh
#---------------------------------------------------------
lec04_파일입출력함수_lkh.uprint(55)
lec04_파일입출력함수_lkh.MemberClass.add("park", 29)  #----비추


#---------------------------------------------------------
from python_basic import lec04_파일입출력함수_lkh as lkh
#---------------------------------------------------------
lkh.uprint(55)
