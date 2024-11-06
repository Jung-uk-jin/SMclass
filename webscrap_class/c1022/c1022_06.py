import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


#순위, 사진링크주소, 제목, 가수명 

data = soup.select_one("#conts")
news = data.select("span")
print(data.select_one("span.rank").next.text,data.select_one("span>a").next.text)


