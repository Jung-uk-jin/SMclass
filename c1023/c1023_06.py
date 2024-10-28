import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import random
url = "http://www.naver.com"
browser = webdriver.Chrome()
browser.get(url)

elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
elem.click()
time.sleep(random.randint(2,5))

#자바 스크립트 호풀 방법
id = "ukjin32"
input_js = 'document.getElementById("id").value = {id}'

elem = browser.find_element(By.ID,"id")
elem.send_keys("ukjin32")
time.sleep(random.randint(2,5))

elem = browser.find_element(By.ID,"pw")
elem.send_keys("1111")
time.sleep(random.randint(2,5))

elem = browser.find_element(By.CLASS_NAME,"btn_login")
elem.click()