import requests
from bs4 import BeautifulSoup
url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("c1021/1.html", "w", encoding= "utf-8") as f:
  f.write(res.text)

#html,css 정보를 가진 소스변경

#태그 출력, 태그 글자 출력
soup = BeautifulSoup(res.text,"lxml") # str -> html,css 태그 사용할수 있는 태그
print(soup.title) #title태그 출력
print(soup.title.get_text()) # 태그 문자열 출력 -text, get_text()

print("없는태그 : ",soup.titletitle) # 없을 시 none
#print("없는태그 : ",soup.titletitle.text) # 없을 시 에러

print(soup.a) # a태그 첫번째 것을 가져옴
print(soup.a.next.text) # next 다음 태그를 가져옴
print(soup.a.attrs) #태그의 속상값 가져옴 : 딕셔너리 형태
print(soup.a["href"]) #a태그의 속성값 가져옴

print(soup.find("div",attrs={"id":"header"}))  # id header인 div태그
print(soup.find("h2",attrs={"class":"rankingnews_tit"}).text) # 
print(len(soup.find_all("div"))) # 모든 div 출력
print(type(soup.find_all("div"))) # 모든 div 출력

# with open("c1021/2.html", "w", encoding= "utf-8") as f:
#   #(soup.prettify()) > 소스가 정리되어 출력
#   f.write(soup.prettify())

print("완료")


