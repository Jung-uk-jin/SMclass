from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random
url = "https://flight.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

browser.get(url)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b')
elem.click()

elem = browser.find_element(By.CLASS_NAME,"autocomplete_input__qbYlb")
elem.send_keys("김포")

elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[9]/div[2]/section/ul/li[2]/a/b')
elem.click()

time.sleep(100)