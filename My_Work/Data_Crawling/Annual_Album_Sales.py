from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

chrome_options.add_experimental_option("excludeSwitches",["enable-loggin"])

driver = wd.Chrome(options=chrome_options)

for i in range(2019,2020):
    try :
        url = f'https://circlechart.kr/page_chart/album.circle?nationGbn=T&targetTime={str(i)}&hitYear={str(i)}&termGbn=year&yearTime=3'
        header = {
            'User-Agent': 'Moaila/5.0'
        }
        driver.get(url)

        html = driver.page_source
        soup = BeautifulSoup(html,'lxml')

        # day = soup.find('div', class_='text-sm font-bold mt-2', id='ChartDateTitle_MO')
        # day = list(day)

        time.sleep(20)

        ranks = soup.find_all('span', class_='font-bold text-sm')
        time.sleep(20)

        titles = soup.find_all('div',class_ ='text-sm font-bold')
        time.sleep(20)

        artists = soup.find_all('div',class_ ='text-sm text-gray-400')
        time.sleep(20)
        
        sales_amounts = soup.find_all('span', class_='font-bold', style="font-family: system-ui;")
        time.sleep(20)

        # for rank, title, artist, sales_amount in zip(ranks,titles,artists,sales_amounts) : 
        #     print(rank.test,title.text,artist.text,sales_amount.text)
        # time.sleep(20)    

        import pandas as pd

        rank_list = [rank.text for rank in ranks]
        title_list = [title.text for title in titles]
        artist_list = [artist.text for artist in artists]
        sales_amount_list = [sales_amount.text for sales_amount in sales_amounts]

        result = pd.DataFrame({'rank' : rank_list,'title': title_list, 'artist':artist_list,'sales_amount':sales_amount_list})
        result.to_excel(f'{str(i)}.xlsx', index =False)

        print(f'{str(i)}.xlsx 완료')


        # result = pd.DataFrame({'rank' : rank_list,'title': title_list, 'artist':artist_list,'sales_amount':amount_list})
        # result.to_excel(f'{day[0]} 기준 앨범판매량 크롤링.xlsx', index =False)

    except :
        pass