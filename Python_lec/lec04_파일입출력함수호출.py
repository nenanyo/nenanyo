# 함수를 불러서 사용  --> 함수 호출
# 함수에 return이 있는 경우 변수에 바인딩해 사용할 수 있다.
# import : 클래스명, 함수명, 모듈명
##------------------------------------------------------------------------
from Python_basic.lec04_파일입출력함수 import TestClass
from Python_basic.lec04_파일입출력함수 import MemClass
from Python_basic.lec04_파일입출력함수 import myprint,uprint
# import 뒤에 ,연결 여러개 동시에

from Python_basic import lec04_파일입출력함수 as 함수
함수.uprint(55)
#전체 클래스 다 가져온다, alias 사용가능(클래스의 alias는 사용x)
# test.lec04_파일입출력함수.py TestClass add()
# a = TestClass.add(1,5)
# print(a)
# print(TestClass.add(1,5))
# myprint(5)