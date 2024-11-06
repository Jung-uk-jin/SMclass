#flight.html 금액이 50000원 미만 항공권 출력
# 김포 - 제주 항공권 개수 : 
# 제주 - 김포 항공권 개수 : 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random
url = "https://flight.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
soup = BeautifulSoup(res.text,"lxml")

data = soup.select_one("#__next > div > main > div.domestic_flight_content__vYDHd > div > div.domestic_results__gp5WB")
stocks = data.select("class.domestic_num__ShOub")
print(stocks)
