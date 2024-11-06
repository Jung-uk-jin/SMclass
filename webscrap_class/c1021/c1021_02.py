import requests
res = requests.get("http://www.google.com")

res.raise_for_status()

print(res.text)

with open("b.html","w",encoding='utf-8') as f:
  f.write(res.text)