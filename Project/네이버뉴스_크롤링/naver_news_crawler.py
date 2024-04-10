import numpy as np
import pandas as pd
import json
from bs4 import BeautifulSoup
import requests
import random
import time
import re
from tqdm import tqdm
from datetime import datetime
import os

class Naver_Crawler:


    def __init__(self):
        self.first_url = 'https://s.search.naver.com/p/newssearch/search.naver?&de={}&ds={}&mynews=1&news_office_checked={}&office_type=1&pd=3&query={}&sort=0&where=news_tab_api&start='

        self.crawl_nexturl_headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
        }

        self.crawl_url_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            ,"Sec-Ch-Ua" :'"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"'
            ,"Sec-Ch-Ua-Arch" :'"x86"'
            ,"Sec-Ch-Ua-Bitness" :'"64"'
            ,"Sec-Ch-Ua-Full-Version-List" :'"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.189", "Chromium";v="121.0.6167.189"'
            ,"Sec-Ch-Ua-Mobile" :'?0'
            ,"Sec-Ch-Ua-Model" :'""'
            ,"Sec-Ch-Ua-Platform" :'"Windows"'
            ,"Sec-Ch-Ua-Platform-Version" :'"10.0.0"'
            ,"Sec-Ch-Ua-Wow64" :'?0'
            ,"Sec-Fetch-Dest" :'document'
            ,"Sec-Fetch-Mode" :'navigate'
            ,"Sec-Fetch-Site" :'same-origin'
        }

        self.crawl_news_headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
            ,"Sec-Ch-Ua":'"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"'
            ,"Sec-Ch-Ua-Mobile":'?0'
            ,"Sec-Ch-Ua-Platform":'"Windows"'
            ,"Sec-Fetch-Dest":'script'
            ,"Sec-Fetch-Mode":'no-cors'
            ,"Sec-Fetch-Site":'same-site'
         }



    def set_params(self, **kwargs): #de, ds, news_name, keyword, save_path
        '''
        크롤링 위한 파라미터 지정
        {de : 크롤링 범위 마지막 날짜(yyyy.mm.dd),
        ds : 크롤링 범위 시작 날짜(yyyy.mm.dd),
        news_name : 신문사 이름,
        keyword : 기사 검색 키워드,
        save_file : csv 저장 경로
        }
        '''
        if "keyword" not in kwargs.keys():
            raise Exception("검색어를 입력해 주세요")
        self.de = kwargs["de"]
        self.ds = kwargs["ds"]
        if "news_name" not in kwargs.keys():
            self.news_code = ""                  # 신문사 이름 입력안하면 전체신문사 뉴스 크롤링
            self.news_name = ""
        else:
            self.news_name = kwargs["news_name"]
            news_code_df = pd.read_csv("./naver_news_code.csv")
            self.news_code = news_code_df['코드'][news_code_df['언론사']==f'{self.news_name}'].values[0]
            self.news_code = str(self.news_code)
        
        if kwargs["keyword"] == "":
            raise Exception("검색어를 입력해 주세요")
       
        else:
            self.keyword = kwargs["keyword"]

        save_base_path = os.getcwd() + '/' + "Crawling_File"

        if "save_file" in kwargs.keys():
            self.save_file = kwargs["save_file"]
        elif "save_file" not in kwargs.keys():
            os.mkdir(save_base_path)
            self.save_file = save_base_path

        # self.save_file = (f'./naver_{self.news_name}_{self.keyword}_{self.ds}{self.de}.csv')





# 크롤링코드
        
    def crawl_nexturl(self):
        '''
        nexturl(url있는 페이지)에서 url 크롤링
        '''
        url_list =[]    # nexturl 담을 리스트
        crawling_bool = True # while문 조건
        start_num = 1        # 1번 기사부터

        first_url = self.first_url.format(
            self.de, self.ds, self.news_code, self.keyword
            )
        while crawling_bool == True:
            interval = np.random.randint(1,2)
            time.sleep(interval)                            # 차단을 방지하기 위한 슬립
            url_fin = first_url + str(start_num) 
            response = requests.get(url_fin, headers=self.crawl_nexturl_headers)
            url_list.append(url_fin)
            if response.status_code == 200:
        
            # 다음 nextUrl이 있는지 확인
                data = response.json()
                next_url = data.get("nextUrl")
                if len(next_url) !=0:                        #  다음 url 페이지가 있다면
                    start_num += 10                            
                    
                else:                                        #  다음 url 페이지가 없다면
                    print('url 페이지로딩을 완료하였습니다')
                    crawling_bool = False                    # while문 종료
            else:
                print('nexturl 페이지 로딩 실패')
                crawling_bool = False 
        # print(url_list)
        return url_list
            
       
            
            
    def crawl_url(self,url_list):
        '''
        뉴스 url 크롤링
        {news_list : 기사 url 담을 리스트}
        '''
        news_list = [] 
        for url in tqdm(url_list): 
    
            interval = np.random.randint(1,2)
            time.sleep(interval)                            # 차단을 방지하기 위한 슬립

            response = requests.get(url, headers=self.crawl_url_headers)
            if response.status_code == 200:
                
                soup = BeautifulSoup(response.text, 'html.parser')            
                li_list=soup.select('li', class_='bx')     
                    
                for item in li_list:
                    try:
                        # print(item)
                        news_href = item.find('a',class_ = "\\\"info\\\"")['href']  # 각각의 기사 url 변수
                        
                        news_href_fin = news_href.replace("\"","").replace("\\","")
                    
                        news_list.append(news_href_fin)
                    except:
                        continue
            else:
                print('기사 url 크롤링 에러')
        # print(news_list)
        return news_list

      
    def crawl_news(self,news_list):
        '''
        기사본문 크롤링
        {news_dict : 뉴스 본문 담을 dict
        , fin_list : 뉴스 딕트 담을 최종 list
        , news_body : 일반/연예 뉴스 구분 변수 (gen:일반/ent:엔터)
        }
        '''
        fin_list = []
        for news in tqdm(news_list):
            news_dict = {}   # 기사 본문 담을 dict
            interval = np.random.randint(1,2)
            time.sleep(interval)                            # 차단을 방지하기 위한 슬립

            response = requests.get(news, headers=self.crawl_news_headers)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                
                # 일반 - 연예뉴스 구분
                body_element = soup.find("body")                
                body_id = body_element.get("id")
                # print(body_id)
                if body_id == "ent_body":
                    news_body = 'ent'
                else:
                    news_body = 'gen'
                # print(news_body)
                # print("news_body:", news_body) 
                # print(news)
                
                

                               
                # 일반뉴스                    
                if news_body == 'gen':
                    # id(f"{oid}{aid}")
                    url_list = list(news.split('/'))
                    oid = url_list[-2]
                    aid = url_list[-1][:10]                    
                    id = f'naver{oid}{aid}'

                    # type
                    type_news = 'news'

                    # reg_date                    
                    now = datetime.now()
                    reg_date = now.strftime('%Y-%m-%d')

                    # inp_date
                    inp= soup.select_one('#ct > div.media_end_head.go_trans > div.media_end_head_info.nv_notrans > div.media_end_head_info_datestamp > div > span').text
                    inp_date = pd.to_datetime(inp.split()[0].replace(".",""),format='%Y%m%d')
                    # print(inp_date)
                    inp_date = inp_date.strftime('%Y-%m-%d')  

                    # title
                    title=soup.find('h2', class_='media_end_head_headline').text   

                    # content                                  
                    content_paragraphs = soup.find("div", class_ = "newsct_article").text
                    content = content_paragraphs.strip().replace("\n","")       

                    # origin_nm                                  
                    origin_nm = soup.find('a', class_="media_end_head_top_logo _LAZY_LOADING_ERROR_HIDE").find('img')['title']

                    # origin_url
                    origin_url = news

                    

                # 연예뉴스
                elif news_body == 'ent':
                    # # id(f"{oid}{aid}")
                    # url_list = list(news.split('='))
                    # oid_int = url_list[1][:2]
                    # aid_int = url_list[2]
                    # print(oid_int,aid_int)
                    # id = f'naver{oid_int}{aid_int}' 
                    # print(id)    
                      # id(f"{oid}{aid}")
                    url_list = list(news.split('/'))
                    oid = url_list[-2]
                    aid = url_list[-1][:10]                    
                    id = f'naver{oid}{aid}'                               

                    #type
                    type_news = 'news'

                    # reg_date                    
                    now = datetime.now()
                    reg_date = now.strftime('%Y-%m-%d')      
                
                    # inp_date       
                    inp = soup.select_one('#content > div.end_ct > div > div.article_info > span > em').text
                    inp_date = pd.to_datetime(inp.split()[0])
                    inp_date = inp_date.strftime('%Y-%m-%d')
                    # print(inp_date)

                    # title
                    title=soup.find('h2', class_='end_tit').text
                    title = title.strip("\n\t\t")
                    # print(title)
                
                    # content
                    content_paragraphs = soup.find("div", class_ = "article_body font1 size3").text
                    content = content_paragraphs.strip().replace("\n","").replace('/','')
                    # print(content)

                    # origin_nm 
                    origin_nm = soup.find('a', class_="press_logo").find('img')['alt']
                    # print(origin_nm)

                    # origin_url
                    origin_url = news
                    # print(origin_url)

                  
                       
                else:
                    print(f'{news}크롤링에 실패했습니다.')
                    continue

            
              #news_dict
                news_dict['id'] = id
                news_dict['type'] = type_news
                news_dict['reg_date'] = reg_date
                news_dict['inp_date'] = inp_date
                news_dict['title'] = title
                news_dict['content'] = content
                news_dict['origin_nm'] = origin_nm
                news_dict['origin_url'] = origin_url                
                fin_list.append(news_dict)     # id, type, reg_date, inp_date, title, content, origin_nm, origin_url                
                
            else:
                print('사이트 접속 불가')
        return fin_list

           

    def crawl(self):
        '''
        크롤링 실행 + csv 저장 함수
        '''
        print("Start Crawling")
        start = datetime.now()

        url_list = self.crawl_nexturl()
        news_list = self.crawl_url(url_list)
        fin_list = self.crawl_news(news_list)
        df = pd.DataFrame(fin_list)

        date_obj_ds = datetime.strptime(self.ds, "%Y.%m.%d") # datetime 으로
        formatted_date_ds = date_obj_ds.strftime("%Y%m%d")   # 문자열로
        date_obj_de = datetime.strptime(self.de, "%Y.%m.%d")
        formatted_date_de = date_obj_de.strftime("%Y%m%d")

        csv_save = self.save_file + f'/naver_{self.news_name}_{self.keyword}_{formatted_date_ds}_{formatted_date_de}.csv'
        df.to_csv(csv_save, encoding = 'utf-8', index = False)

        print(f'{self.save_file}에 저장되었습니다.')
        print('코드실행시간: ', datetime.now() -  start)


# Test
crawler = Naver_Crawler()
crawler.set_params(ds = '2024.02.20',
                de = '2024.02.29',                
                keyword = '제니',
                save_file = 'c:/AI',
                news_name = '데일리안'
                )

crawler.crawl()




