from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options
import pyautogui

#제목 금액 평점 평가수 찜 정보 1-5페이지
#평점 4.8이상 평가수 1000명이상 상품을 csv파일로 저장
# browser = webdriver.Chrome()
# browser.maximize_window()
# for i in range(1,6):
#   url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
#   browser.get(url)
#   time.sleep(2)
#   prev_height = browser.execute_script("return document.body.scrollHeight")
#   while True:
#    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#    #페이지가 로딩되면서 길어진 길이를 다시 가져옴
#    curr_height = browser.execute_script("return document.body.scrollHeight")
#    if prev_height == curr_height:
#      break
#    prev_height = curr_height
#    time.sleep(5)
  # soup = BeautifulSoup(browser.page_source,"lxml")
  # with open(f'c1025/market{i}.html','w',encoding='utf-8') as f:
  #   f.write(soup.prettify())
# 파일 불러와서 soup파싱

with open('c1025/market1.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f,"lxml")

data = soup.select_one("#content > div.style_content__xWg5l")
lists = data.select("div.adProduct_item__1zC9h")
for list in lists:
  score = list.select_one("span.adProduct_rating__PaMzh").text.strip()
  print(score)


