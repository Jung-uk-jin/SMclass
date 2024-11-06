from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
with open('c1025/navershop1.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f,"lxml")
# 기준점
data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div")
pro_lists = data.select(".adProduct_item__1zC9h")
# print(pro_lists[1])
    # csv파일로 저장(중요)   
f = open("c1025/nshop.csv",'a',encoding="utf-8-sig",newline="")
writer = csv.writer(f)
#광고상품
# for i,pro_list in enumerate(pro_lists):
#   print(f"{i+1}.")
#   try:
#     # 1. 제목
#     title = pro_list.select_one("div.adProduct_title__amInq > a").text.strip()
#     print(title)
#     # 2. 금액 - 정수형타입변경
#     price = int(pro_list.select_one("div.adProduct_price_area__yA7Ad > strong > span.price > span > em").text.strip().replace(",",""))
#     print(price)
#     # 3. 평점
#     rating = float(pro_list.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > span.adProduct_rating__PaMzh").text.strip())
#     print(rating)
#     # 4. 평가수
#     a_count = int(pro_list.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > em").text.replace(",","").strip())
#     print(a_count)
#     # 5. 찜수
#     c_count = int(pro_list.select_one("div.adProduct_etc_box__UJJ90 > span:nth-child(2) > span").text.replace(",","").strip())
#     print(c_count)
#     print("-"*50)
#    # 생성된 정보 집어넣기
#     writer.writerow([title,price,rating,a_count,c_count]) 
#   except:
#     print("예외처리")
#t실제 상품
pro_lists = data.select(".product_item__MDtDF")
print("개수 :",len(pro_lists))
for i,pro_list in enumerate(pro_lists):
  try:
    print(f"{i+1}.")
    title = pro_list.select_one("div.product_title__Mmw2K").text.strip()
    print(title)
    price = (pro_list.select_one("span.price_num__S2p_v").text.strip().replace(",","").replace("원",""))
    print(price)
    rating = (pro_list.select_one("span.product_grade__IzyU3").text.replace(" ","").replace("\n","").replace("별점",""))
    print(rating)
    a_count = (pro_list.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(3) > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_etc_box__ElfVA > a > em").text.strip().replace(" ","").replace("\n","").replace("(","").replace(")",""))
    if '만' in a_count: a_count = float(a_count[:-1])*10000
    else: a_count=float(a_count)
    print(a_count)
    c_count = (pro_list.select_one("span.product_num__fafe5").text.replace(",","").strip())
    print(c_count)
  except:
    print("예외처리")
f.close()