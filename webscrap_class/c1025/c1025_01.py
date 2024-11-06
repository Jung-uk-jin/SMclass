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

url = "https://www.naver.com"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

elem = browser.find_element(By.XPATH,'//*[@id="query"]')
elem.click()
elem.send_keys("네이버 쇼핑")
elem.send_keys(Keys.ENTER)
browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a/mark').click()

time.sleep(3)
browser.switch_to.window(browser.window_handles[1])
elem = browser.find_element(By.CLASS_NAME,'_searchInput_search_text_3CUDs')
elem.click()
time.sleep(3)
elem.send_keys("무선 마우스")
elem.send_keys(Keys.ENTER)



input("엔터")

