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

for i in range(2020,2025):
    for k in range(1,54) :

        try :
        
            url = f'https://circlechart.kr/page_chart/onoff.circle?nationGbn=T&serviceGbn=ALL&targetTime={str(k).zfill(2)}&hitYear={str(i)}&termGbn=week&yearTime=3'
            header = {
                'User-Agent': 'Moaila/5.0'
            }
            driver.get(url)

            html = driver.page_source
            soup = BeautifulSoup(html,'lxml')
            time.sleep(20)

            ranks = soup.find_all('span', class_='text-2xl')
            time.sleep(20)

            titles = soup.find_all('div',class_ ='font-bold mb-2')
            time.sleep(20)

            artists_album = soup.find_all('div',class_ ='text-sm text-gray-400 font-bold')
            time.sleep(20)

            import pandas as pd

            rank_list = [rank.text for rank in ranks] # 50개만 가져오기
            title_list = [title.text for title in titles]
            artist_album = [artist_album.text for artist_album in artists_album]
            artist_list = [artist.split('|')[0] for artist in artist_album]
            album_list = [album.split('|')[1] for album in artist_album]

            # if len(rank_list) == 0 :
            #     continue 

            result = pd.DataFrame({'rank' : rank_list,'title': title_list, 'artist':artist_list,'album':album_list})
            result.to_excel(f'{str(i)} Weeks {str(k)}.xlsx', index =False)

            print(f'{str(i)}년 {str(k)}째주 음원 순위 크롤링 완료')

        except :
            pass