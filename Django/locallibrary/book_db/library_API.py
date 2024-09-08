import requests
import pprint
import json
import pandas as pd
import numpy as np
# from pandas.io.json import json_normalize


## 국립중앙도서관 API  ----> 타이틀, 작가 외에 필요한 항목 없음
#pageNum -> 1~10
# pageSize = 10
# key="2daefcef1e882c76a4b442786a77b7000dd826cab763fdca53fa87695025f8e7"
# systemType = "오프라인자료"
# category = '도서'
# apiType = 'json'

# url = "https://www.nl.go.kr/NL/search/openApi/search.do?key=2daefcef1e882c76a4b442786a77b7000dd826cab763fdca53fa87695025f8e7&apiType=json&pageSize=10&pageNum=1&kwd=서울&systemType=오프라인자료"

# response= requests.get(url)
# contents = response.text
# pp = pprint.PrettyPrinter(indent=4)
# # print(pp.pprint(contents))

# json_ob = json.loads(contents)
# body = json_ob['result']
# # print(body)


# 알라딘 API --------> O

# url = "http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey=ttbblueblue9871416001&CategoryId=1230&QueryType=Bestseller&MaxResults=10&start=1&SearchTarget=Book&output=js&Version=20131101"

# response= requests.get(url)
# contents = response.text
# pp = pprint.PrettyPrinter(indent=4)
# # print(pp.pprint(contents))
# json_ob = json.loads(contents)
# body = json_ob['item']
# print(body)

# dataframe = pd.json_normalize(body)
# # print(dataframe)
# dataframe.to_csv('./DB/books.csv',index=False)

# 카테별로 갖고 오기------------------------------------------------------------------------------------

genre = pd.read_csv('./book_db/Genre_ID.csv')
genre.columns = genre.columns.str.lower()
# print(genre['genre_id'])
books=pd.DataFrame()
for id in genre['genre_id']:
    url = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey=ttbblueblue9871416001&CategoryId=' + str(id) + '&QueryType=Bestseller&MaxResults=10&start=1&SearchTarget=Book&output=js&Version=20131101'
    response= requests.get(url)
    contents = response.text
    pp = pprint.PrettyPrinter(indent=4)

    dict = {}
    json_ob = json.loads(contents)
    body = json_ob['item']
    # dict['']
    # dataframe = pd.json_normalize(body)
    # books = pd.concat([books,dataframe])
print(np.hstack(body))
# books.to_csv('./DB/books_final.csv',index=False)
