# import os
# import sys
# import urllib.request
# client_id = "o4y3sY0slf1OtAqzQqVn"
# client_secret = "UbuoGpu3Cc"
# encText = urllib.parse.quote("art")
# url = "https://openapi.naver.com/v1/search/book.xml?query=" + encText # JSON 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request)
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)


import urllib.request

client_id = "o4y3sY0slf1OtAqzQqVn" # 애플리케이션 등록시 발급 받은 값 입력
client_secret = "UbuoGpu3Cc" # 애플리케이션 등록시 발급 받은 값 입력
encText = urllib.parse.quote("파이썬")
url = "https://openapi.naver.com/v1/search/book?query=" + encText +"&display=3&sort=count"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)