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

# selenium 화면을 숨김처리
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")


url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)

soup = BeautifulSoup(browser.page_source,"lxml")
data = soup.select_one("#detected_value").text
print(data)
input("엔터키 입력 완료")
#for i in range(1,4):  
#  url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i}"
#  browser = webdriver.Chrome()
#  browser.maximize_window()
#  browser.get(url)
#  time.sleep(3)
#  soup = BeautifulSoup(browser.page_source,"lxml") # 페이지 가져오기 (중요)
#  with open(f"c1024/gmarket{i}.html","w",encoding='utf-8') as f:
#    f.write(soup.prettify()) # 파일 저장

input("엔터키 입력 완료")
for i in range(1,4):
    with open(f"c1024/gmarket{i}.html","r",encoding='utf-8') as f:
     soup = BeautifulSoup(f,"lxml") # 파일 출력





