a='A'
b='B'
print(a+b)

## 따옴표, 쌍따옴표 구분 X
## + : 수치는 계산/글자는 합치기
## * : 숫자*숫자는 계산/(글자 * 숫자)는 반복
## 함수 대문자 X
## 변수 숫자로 시작X

A = 'ABC'
B = 3
print(A*B)


#리스트 [] : 다양한 타입의 값 넣을 수 있다
# a = [1,2,3,4, 'x']  # ---컬렉션, 값의 접근 인덱스 0번째
# a[4] = 'z'
# # n번째 값 수정
# a.append(6)  # 1234'x'6 ---값 추가하기
# #a.remove('x')  #1  2346 --- 값 제거하기
# del a [0] ---0번째 값 지워라
# a.insert(1,"BBB") #1BBB2346
# # n번째에 , 특정값을 넣어줘
# a.pop(0) #'BBB' 2346
# # n번째 값 지워줘
#
# print(a)
#
# A = [1,2,3,'AA',5,{"name":"홍길동", "tel": "010"}]
##--A.pop()   --젤 뒤에거 지워
##--A.pop(0) --0번째
##--A.remove('AA') -- 특정값 지워
##--del A[0]-- 0번째 지워
# print(A)

#print(a[4])
# a의 4번째 값 출력
# __붙은 함수는 특이성함수

#
# #튜플() : 리스트의 상수형, 중간에 값 수정 불가능하게 데이터 교환, 조회용으로만
# # b.apppend - 불가능
# b = (1,2,3,4,5)
# print (b[2])
#
# #딕셔너리 {키 : 값, 키 : 값, 키 : 값}
# d = {"empno" : 7733, "ename" : "smith" }
#
# print(d["ename"]) #-----select
# d["job"] = "sales"
# ## 새로운 키, 값 추가 ------insert
# d["ename"] = "ssmith"
# ## 기존의 키의 값 변경--------update
# print(d)
#

#mem = [1,2,3, ['A','B']]

#mem = [1,2,3, ('A','B')]
#print(mem)
#print(mem[3][1])--- 리스트, 튜플 같음
#mem = [1,2,3, {'empno':'7733', 'ename' : 'smith'}]
#print(mem[3]['empno'])

###타입
print(type(5),5)
print(type('abc'),'abc')
print(type(17.4))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({'empno':7777}))
print(type((True)))
##true false : 불리언(bool)

##캐스팅: casting, 형변환, 타입변환
print(3+int('4'))
print(str(3)+str(4)) #34
print(4 + float(3))
##---더 큰 범위인 실수따라간다, 헷갈리면 둘다 캐스팅

#----------------------슬라이싱(slicing) : 문자, 리스트 가능
#[시작이상 : 끝미만 : 1정방/-1거꾸로]

msg = 'ABCDE'
print(msg[0:2])
print(msg[3:5])
## =print(msg[3:])  > 뒤에꺼 다가져와
##print(msg[-2:])

emps = [7733,7822,7922,8000]
print(emps[1:3])


license_plate = "24가 2210"
print(license_plate[-4:])
## 뒤에서 4자리부터

STRING = "홀짝홀짝홀짝"
print(STRING[::2])

string = "PYTHON"
print(string[::-1])

PN = '010-1111-2222'
print(PN[0:3],PN[4:8],PN[-4:])
# PN = PN.replace("-"," ")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

### strip() ------좌우의 공백제거/'삼성' '전자'사이의 공백은 그대로
data = "        삼성 전자      "
data1 = data.strip()
print(data1)

##split : 구분자 단위로 문자열 자르기
a = "hello world"
print(a.split( ),type(a.split( )))

tel = '010-1234-5678'
print(tel.split('-'),tel.split('-')[1])

##리스트 합치기
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang3  = lang1 + lang2
print(lang3)

print(len(lang3))
## len() : 갯수세기
lang1.extend(lang2)
print(lang1)
lang1.append(lang2)
##-- 합치지만 모양이 다름

## ------- site의 rest api
ytb = {
 "kind": "youtube#videoListResponse",
 "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/sDAlsG9NGKfr6v5AlPZKSEZdtqA\"",
 "videos": [
  {
   "id": "7lCDEYXw3mM",
   "kind": "youtube#video",
   "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/iYynQR8AtacsFUwWmrVaw4Smb_Q\"",
   "snippet": {
    "publishedAt": "2012-06-20T22:45:24.000Z",
    "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "title": "Google I/O 101: Q&A On Using Google APIs",
    "description": "Antonio Fuentes speaks to us and takes questions on working with Google APIs and OAuth 2.0.",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/default.jpg"
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/mqdefault.jpg"
     },
     "high": {
      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/hqdefault.jpg"
     }
    },
    "categoryId": "28"
   },
   "contentDetails": {
    "duration": "PT15M51S",
    "aspectRatio": "RATIO_16_9"
   },
   "statistics": {
    "viewCount": "3057",
    "likeCount": "25",
    "dislikeCount": "0",
    "favoriteCount": "17",
    "commentCount": "12"
   },
   "status": {
    "uploadStatus": "STATUS_PROCESSED",
    "privacyStatus": "PRIVACY_PUBLIC"
   }
  }
 ]
}
# print(ytb["videos"][0]["snippet"]["title"])
# print(ytb["videos"][0]["snippet"]["thumbnails"]["default"]["url"])
# print(ytb["videos"][0]["statistics"]["viewCount"])

naver = {
  "urls": [
    {
      "url": "http://www.your-site.com/article-1",
      "type": "update"
    },
    {
      "url": "http://www.your-site.com/article-2",
      "type": "update"
    },
    {
      "url": "http://www.your-site.com/article-3",
      "type": "delete"
    },
    {
      "url": "http://www.your-site.com/article-4",
      "type": "delete"
    }
  ]
}
# print(naver["urls"][2]["url"])
# print(naver["urls"][3]["url"])


