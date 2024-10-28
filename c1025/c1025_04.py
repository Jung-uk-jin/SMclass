from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
import csv

with open('c1025/navershop1.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f,"lxml")

#기준점
data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div")
pro_lists = data.select("div.adProduct_item__1zC9h")

for i,pro_list in enumerate(pro_lists):
    print(f"{i+1}번 품목")
  # #1.제목
  # try:
    title = pro_list.select_one("div.adProduct_title__amInq > a").text.strip()
    print(title)
  #   #2.금액
    price = pro_list.select_one("div.adProduct_price_area__yA7Ad > strong > span.price > span > em").text.strip().replace(",","")
    print(int(price))
  #   #3. 평점
    rating = pro_list.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > span.adProduct_rating__PaMzh").text.strip()
    print(float(rating))
  #   #4.평가수
  #   count = pro_list[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div.adProduct_info_area__dTSZf > div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > em").text.replace(",","").strip()
  #   print(int(count))
  #   #5. 찜 수
  #   c_count = pro_list[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div.adProduct_info_area__dTSZf > div.adProduct_etc_box__UJJ90 > span:nth-child(2) > span").text.strip()
  #   print(int(c_count))
    print("--------------------------")
  # except:
  #  print("예외처리")

