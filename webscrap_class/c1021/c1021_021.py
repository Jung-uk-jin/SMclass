import requests

url="http://www.melon.com"
headers = {"User-Agent!": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
print("ㅋ드 상태 : ",res.status_code)
res.raise_for_status()


with open("b.html","w",encoding='utf-8') as f:
  f.write(res.text)