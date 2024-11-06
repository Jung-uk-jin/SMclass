import os
import requests
from bs4 import BeautifulSoup
import time
import csv

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")
#print(len(stocks)) # tr의 개수
# print(stocks[0].select("th")) # tr의 0번째의 th를 출력
# 상단 타이틀
f=open("c1023/stock.csv","w",encoding="utf-8-sig",newline="")
writer = csv.writer(f)
st_list=[st.text for st in stocks[0].select("th")] # 배열 선언  / 결과값 / 반복문 선언
writer.writerow(st_list)
print(st_list)
print(len(st_list)) # 항목 : 12개

for stock in stocks:
  sts = stock.select("td")
  if len(sts) <= 1: continue
  sto_list = [ st.text.strip().replace("\t","").replace("\n","")  for st in sts ]
  writer.writerow(sto_list) # 리스트타입 저장 가능
  print(sto_list)
f.close()
print("완료")
#1번쨰
# print(stocks[1].select("td")) # 항목 1개
# print(stocks[2].select("td"))
# print(len(stocks[2].select("td")))


# data_list=[]
# # 30개의 정보를 csv파일로 저장
# for i in range(2,7):
#   sto_list=[sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[i].select("td")] # 배열 선언  / 결과값 / 반복문 선언
#   data_list.append(sto_list)
#   # print(sto_list)  
# for i in range(10,15):
#   sto_list=[sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[i].select("td")] # 배열 선언  / 결과값 / 반복문 선언
#   data_list.append(sto_list)
#   # print(sto_list)  
# for i in range(18,23):
#   sto_list=[sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[i].select("td")] # 배열 선언  / 결과값 / 반복문 선언
#   data_list.append(sto_list)
#   # print(sto_list)  
# for i in range(26,31):
#   sto_list=[sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[i].select("td")] # 배열 선언  / 결과값 / 반복문 선언
#   data_list.append(sto_list)
#   # print(sto_list)  
# for i in range(34,39):
#   sto_list=[sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[i].select("td")] # 배열 선언  / 결과값 / 반복문 선언
#   data_list.append(sto_list)
#   # print(sto_list)  
# for i in range(42,47):
#   sto_list=[sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[i].select("td")] # 배열 선언  / 결과값 / 반복문 선언
#   data_list.append(sto_list)
#   # print(sto_list)  
# print(data_list)


# #리스트 생성
# sts = stocks[0].select("th") # stock(tr의 0번째 데이터) 중 th
# for st in sts:
#   print(st.text)
#   st_list.append(st.text)
# print(st_list)

