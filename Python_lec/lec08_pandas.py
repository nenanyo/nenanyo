# interprinter : 한줄 한줄씩 출력
# 마운트 : 접속,연결
# 구글드라이브에서 코랩으로 연결 할 수도
# 코랩  - 온라인 파이참 연습
# 위키독 - 개발자가 만든 설명서
# reshaping - 행과 열 변화 (3행 2열) > (2행 3열)
#
# 열(1줄) - 1 demension series
# □
# □
# □
# □

#  (행,열) -  2 demension series , data frame
# □□
# □□
# □□
# □□
#
# Nan(결측) = null
#
# SAS(세스) : 테라급 파일 통계 패키지
#  - 마곡 인젠트회사가 한국sas 임원들이 차린 진짜배기
#
# jupiter lab 실행한 지점에서 하위폴더로만 갈수 있다 > 실행시킬 지점을 가장 상위폴더로 하자
#
# pandas, numpy는 외부패키지, import 해서 쓴다

#


import pandas as pd
import numpy as np

print(pd.Series([1,2,np.nan, 3,4]))
###np.nan : 결측

# pd.date_range(시작일, 주기)
# dtype = [ns] : 나노세컨즈,freq = "주기"
#index는 colunm이름 없다
a = np.random.randn(6,4)
print(type(a))
#넘피 array 행과열을 가진 배열, 리스트처럼 생겨서 ',' 없다/<class 'numpy.ndarray'>
#pd.categorical(["소","중","대"]) : 텍스트로 된 분류
#타입 : float, int - 8,16,32,64/범위의 차이
# head()/tail() : 앞에서,뒤에서 5개
# 피벗 - 행과열 전환
# ["":""] - 값은 이상,이하
# [:] - 범위는 이상,미만

# pd.Series([리스트성 객체]) : 열로 만들어줌/리스트, 튜플,딕셔너리,numpy.ndarray
#정렬 - df.sort_index()/df.sort_values(by="B")
#loc/iloc/ - select, 단일값, 슬라이싱, 리스트
#at -update
#s.str.lower() - str해야 글자로 인식

##df과 series합칠때 인덱스가 같아야 함
## 평균 mean
