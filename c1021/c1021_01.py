#웹 스크래핑 세팅

import requests
res = requests.get("http://www.google.com/") # html소스 가져옴
res2 = requests.get("http://www.naver.com/") # html소스 가져옴
res.raise_for_status() # 에러시 종료
print(res.text)

#requests 정보를 가져올시 제이쿼리, 자바스크립트, 외부페이지,react 등 효과는 가져올수 없다
# 비동기식으로 작동되는 파일이기 때문

print("총 문자 길이 : ",len(res2.text))


#웹 소스코드 파일 저장
#f = open("a.html","w",encoding="utf-8")
#f.write(res.text)
#f.close()

#f.close() 안해도 됨
# with open("c1021/c.html","w",encoding='utf-8') as f:
#   f.write(res.text)

# if res.status_code==200:
#   print(res.text) # html소스 출력
# else:
#   print("접근할 수 없다")
# print("응답코드 : ", res.status_code) # 200
# print(res.text)