from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random
url = "http://www.daum.net"

browser = webdriver.Chrome() # 크롬 브라우저 열기
browser.get(url) # url 사이트 접속

elem = browser.find_element(By.CLASS_NAME,"btn_login") # 클래스 이름이 로그인인거 찾기

elem.click() # 버튼 클릭
time.sleep(random.randint(2,5)) # 대기

# 아이디와 패스워드의 id를 찾아서 입력 후 값 설정
input_js = 'document.getElementById("loginId--1").value="{id}";\
  document.getElementById("password--2").value = "{pw}";'.format(id="onulee",pw="j")

browser.execute_script(input_js) # 실행
time.sleep(random.randint(2,5))

# 로그인  
elem = browser.find_element(By.CLASS_NAME,"btn_g highlight submit")
elem.click()
time.sleep(random.randint(2,5))