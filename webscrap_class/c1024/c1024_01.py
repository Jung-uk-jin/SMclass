from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time
import requests
from bs4 import BeautifulSoup
import random

url = "https://www.yanolja.com/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

#검색창 클릭 Xpath 가져오기
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]/div/div').click()
# time.sleep(3)
# #날자 선택
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()
# time.sleep(3)
# #시작 날짜
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
# time.sleep(3)
# #끝날짜
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]').click()
# time.sleep(3)
# #확인버튼
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button').click()
# time.sleep(3)
# #검색창 클릭
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
# time.sleep(3)
# elem.click()
# time.sleep(3)
# #글자 입력
# elem.send_keys("강릉 호텔")
# time.sleep(3)
# #엔터기 입력 
# elem.send_keys(Keys.ENTER) 
# time.sleep(3)
# #자동시 로딩 대기
# #화면의 호탤검색내용이 뜰 때까지 대기, 최대 30초 대기
# WebDriverWait(browser,30).until(lambda x : x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))

# #화면을 스크롤해서 내리기 반복
# #execute_script : 자바스크립트 실행 함수
# prev_height = browser.execute_script("return document.body.scrollHeight")
# while True:
#   browser.execute_script("windows.scrollTo(0,document.body.scrollHeight)")
#   #페이지가 로딩되면서 길어진 길이를 다시 가져옴
#   curr_height = browser.execute_script("return document.body.scrollHeight")
#   if prev_height == curr_height:
#     break
#   prev_height = curr_height
# print("스크롤 내리기 완료")
soup = BeautifulSoup(browser.page_source,"lxml")
#html파일로 저장
# with open('c1024/yanolja.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())
# #파일 불러와서 soup파싱
# with open('c1024/yanolja.html','r',encoding='utf-8') as f:
#   soup = BeautifulSoup(f,"lxml")
#평점이 4.8이상 금액 17만원 이하
#호텔명 , 평점, 금액, 
#기준점 생성
data = soup.select_one("#__next > div > main > section > div.PlaceListBody_listContainer__2qFG1")
lists = data.select("div.PlaceListItemText_container__fUIgA text-unit PlaceListBody_textItem__1yTQ6 PlaceListBody_noPaddingTop__26Jd8")
print(lists)
input("엔터키를 입력하면 완료됩니다")

