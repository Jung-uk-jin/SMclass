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
options = Options()
options.add_argument("--headlessx")
options.add_argument("window-size=1920,1080")
options.add_argument("User-Agent = from selenium.webdriver.chrome.options import Options")

for i in range(1,4):  
  browser = webdriver.Chrome(options=options)
  browser.maximize_window()
  url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i}"
  browser.get(url)
input("엔터키 입력 : 완료")
  
#노트북 검색된 사이트 1,2,3페이지에서 만족도가 95이상이면서 금액은 1,500,000이하
#평가수가 100 이상
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(1)
#   # 페이지가 로딩되면서 길어진 길이를 다시 가져옴.
  curr_height = browser.execute_script("return document.body.scrollHeight")
#   # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
  if prev_height == curr_height:
     break
   # 더 길이가 길어졌으면, 이전길이에 현재길이를 입력시킴
  prev_height = curr_height
#print("스크롤 내리기 완료")
soup = BeautifulSoup(browser.page_source,"lxml")
with open('c1024/gmarket.html','w',encoding='utf-8') as f:
   f.write(soup.prettify())
input("Enter키를 입력하면 완료됩니다.")
# 파일불러와서 soup으로 파싱
with open('c1024/gmarket.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f,"lxml")
data =  soup.select_one("#section__inner-content-body-container > div:nth-child(4)".strip())
print(data)

  

