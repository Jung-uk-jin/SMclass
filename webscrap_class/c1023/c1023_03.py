import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
#다음사이트에서 검색창에 주식정보를 입력하여 페이지 이동
broswer = webdriver.Chrome() # 크롬 브라우저 열기
broswer.get("https://daum.net") # 사이트 입력
elem = broswer.find_element(By.ID,"q") #사이트 안에 원하는 곳의 id및 클래스 입력
elem.send_keys("주식정보") # 원하는 정보 입력
elem.send_keys(Keys.ENTER) 


broswer.get("https://naver.com")
elem = broswer.find_element(By.CLASS_NAME,"search_input")
elem.send_keys("주식정보")
elem.send_keys(Keys.ENTER)
time.sleep(100) # 시간 지연
# browser = webdriver.Chrome()
# browser.get("https://naver.com")

# elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
# #클릭
# elem.click()#클릭
# browser.back()#뒤로
# browser.forward()#앞
# #html 위치 찾기 - requests.select
# elem = browser.find_element(By.NAME,'pw')

# elem = browser.find_element(By.ID,"query")
# elem.send_keys("네이버 영화")
# time.sleep(100)
# #새창 이동
# browser.switch_to.window(browser.window_handles[1])

