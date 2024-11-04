import pandas as pd
import numpy as np
import requests
import pprint
import json
import uuid

import csv
import os
import django

# raw book data -> formal book data-------------------------------------------------------------
# books = pd.read_csv('./DB/books_final.csv')
# # print(books.columns)
# # print(type(books))
# books_formal = books[['title','author','description','isbn13','categoryId','categoryName']]
# # print(books_formal)
# books_formal.to_csv('./DB/books_formal.csv',index=False)



# Genre data 넣기-------------------------------------------------------------------------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")
django.setup()

from catalog.models import Genre,Author,Book,BookInstance,Language

# f = open('./book_db/Genre_ID.csv','r',encoding='utf-8')
# info = []

# rdr = csv.reader(f)
# for id,name in rdr:
#     # print(id,name)
#     tuple = (id,name)
#     info.append(tuple)
# f.close()

# # info.pop()
# info = info[:31]
# # print(info)

# instances = []
# for (num,name) in info:
#     print(num,name)
#     instances.append(Genre(genre_num = num, name = name))

# # print(instances[-1])
# Genre.objects.bulk_create(instances)   
# 


#  
# Author data 넣기-------------------------------------------------------------------------------
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")
# django.setup()

# f = open('./book_db/DB/books_formal.csv','r',encoding='utf-8')
# raw_authors = []
# rdr = csv.reader(f)
# for row in rdr:
#     author = row[1]
#     author_sp = author.split('(지은이)')
#     raw_authors.append(author_sp[0])
# f.close()

# # 데이터 정제
# # 제 1저자만 남기기
# df = pd.DataFrame(raw_authors,columns = ['author'])
# df = df.drop(index=0)
# df['author_sp'] = df['author'].str.split(',')
# df['author_new'] = df['author_sp'].map(lambda x: x[0] )

# # (엮은이),(원작), (글) 지우기
# clean_list = ['(엮은이)','(원작)','(글)']
# for word in clean_list:
#     df['author_new'] = df['author_new'].str.replace(word,'')
#     df['author_new'] = df['author_new'].str.strip()



# instances = []
# for name in df['author_new']:
#     # print(name)
#     if name not in instances:            # 중복제거
#         # instances.append(Author(name = nm))
#         instances.append(name)



# # print(len(instances))
# hash_instances =[]
# for i in instances:
#     hash_instances.append(Author(name=i))

# print(len(hash_instances))

# # print(instances[-1])
# Author.objects.bulk_create(hash_instances)            



# Genre data 넣기-------------------------------------------------------------------------------
# genre = pd.read_csv('./book_db/Genre_ID.csv')
# genre.columns = genre.columns.str.lower()
# books_list = []
# for id in genre['genre_id']:
#     url = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey=ttbblueblue9871416001&CategoryId=' + str(id) + '&QueryType=Bestseller&MaxResults=10&start=1&SearchTarget=Book&output=js&Version=20131101'
#     response= requests.get(url)
#     contents = response.text
#     pp = pprint.PrettyPrinter(indent=4)
#     json_ob = json.loads(contents)
#     body = json_ob['item']
#     books_list.extend(body)

# instances = []
# for row in books_list:
#     categoryName_list = row['categoryName'].split('>')
#     categoryName = categoryName_list[1]
#     if categoryName not in instances:            # 중복제거
#         instances.append(categoryName)
# # print(instances)
# hash_instances =[]
# for i in instances:
#     hash_instances.append(Genre(name=i))
# print(len(hash_instances))

# print(hash_instances[0],hash_instances[-1])
# Genre.objects.bulk_create(hash_instances) 



# Book data 넣기-------------------------------------------------------------------------------
# API에서 불러서 바로 해볼까...... json-> dict -> bulk create
# genre = pd.read_csv('./book_db/Genre_ID.csv')
# genre.columns = genre.columns.str.lower()
# # print(genre['genre_id'])
# books_list = []
# for id in genre['genre_id']:
#     url = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey=ttbblueblue9871416001&CategoryId=' + str(id) + '&QueryType=Bestseller&MaxResults=10&start=1&SearchTarget=Book&output=js&Version=20131101'
#     response= requests.get(url)
#     contents = response.text
#     pp = pprint.PrettyPrinter(indent=4)
#     json_ob = json.loads(contents)
#     body = json_ob['item']
#     books_list.extend(body)

# # print(len(books_list))

# # 중복제거
# books_list_unique = list({v['isbn13']:v for v in books_list}.values())
# # print(len(books_list_unique))


# instances = []

# for i in books_list_unique:

#     # author 
#     tmp = i['author'].split(' (지은이)')
#     author = tmp[0]
#     author_list = author.split(',')
#     author_new = author_list[0]

#     if '(엮은이)' in (author_new):
#         author_new = author_new.replace('(엮은이)','')
#     elif '(원작)' in (author_new):
#         author_new = author_new.replace('(원작)','')
#     elif '(글)' in (author_new):
#         author_new = author_new.replace('(글)','') 

#     author_instance,created = Author.objects.get_or_create(name=author_new) 
    
#     # genre
#     categoryName_list = i['categoryName'].split('>')
#     categoryName = categoryName_list[1]
#     genre_instance,created  = Genre.objects.get_or_create(name=categoryName)
#     # print(genre_instance)

#     # languange
#     language_instance,created  = Language.objects.get_or_create(name='한국어')

#     Book_Intance= Book(
#         title = i['title'],
#         author = author_instance,
#         summary = i['description'],
#         isbn = i['isbn13'],
#         genre = genre_instance,
#         language = language_instance
#         )

#     instances.append(Book_Intance)
#     book_instances.append(BookInstance(
#     id = uuid.uuid4,
#     book = Book_Intance
#     ))

    # print(book_instances)
# print(instances) 
# print(len(instances))

# Book.objects.bulk_create(instances) 



# BookInstances -----------------------------------------------------------------------------------
book_list = Book.objects.all()


# print(book_list)
# Book_instance,created = Book.objects.get(name=author_new) 

book_instances = []
for row in book_list:
    book_instances.append(BookInstance(
        id = uuid.uuid4(),
        book = row
    ))
# BookInstance.objects.bulk_create(book_instances) 
