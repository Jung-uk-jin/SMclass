from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

for i in range(2020,2024):
  url = f"https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
  # Chrome()안에 chromedriver.exe위치 입력해줘야함
  # root에 파일이 저장되어있으면 입력하지 않아도 됨
  # broswer = webdriver.Chrome()
  # broswer.get(url)
  soup = BeautifulSoup(broswer.page_source,"lxml")
  # 파일저장
  with open(f'c1023/yeogi{i+1}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
# data = soup.select_one("#__next > div > main > section > div.css-1qumol3")
#파일 불러오기 - BeautifulSoup으로 파싱
# with open('c1023/yeogi.html','r',encoding='utf-8') as f:
#  soup = BeautifulSoup(f,'lxml')
# #제목,평점,평가수,금액,이미지,링크주소
data = soup.select_one("#__next > div > main > section > div.css-1qumol3")
sells = data.select("a")

#20개 출력 -> 평가수 500명이하 제외
for idx,sell in enumerate(sells):
  rating = float(sell.select_one("span.css-9ml4lz").text.strip())
  num = sell.select_one("span.css-oj6onp").text.strip()[:-4]
  num = int(num.replace(",",""))
  price = sell.select_one("span.css-5r5920").text.strip()
  price = int(price.replace(",",""))
  image = sell.select_one("div.css css-nl3cnv")
  if num<500 and rating >9.0 and price >120000:
    continue
  print(f"{idx+1}") 
  print("상품명 : " ,sell.select_one("h3").text.strip())
  print("평점 : " ,rating)
  print("평가수 : " ,num)
  print("금액 : " ,price)
  print("----------------------------")







#request로 정보 가져오기
# url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#     'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")

# with open('c1023/yeogi.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())

# data = soup.select_one("#__next > div > main > section > div.css-1qumol3")
