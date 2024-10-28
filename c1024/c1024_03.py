from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random

#for i in range(1,4):  
#  browser = webdriver.Chrome()
#  browser.maximize_window()
#  url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i}"
#  browser.get(url)/