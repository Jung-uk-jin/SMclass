# [ 프로그램 설치 방법 ]
# 1. 파이썬 다운로드
# python 설치
# 환경변수 path 설정
# 2. 라이브러리 설치
# pip install requests
# pip install beautifulsoup4
# pip install lxml
# 3. selenium 설치
# ## chromedriver 크롬 드라이버 다운로드
# https://chromedriver.chromium.org/downloads
# 4. 오라클 라이브러리 설치
# python -m pip install oracledb

import oracledb
#oracle 연결 - sql delvoper 연결
conn = oracledb.connect(user="ora_user", password="1111",dsn="localhost:1521/xe")
#연결 확인
print(conn.version)
#sql 실행창 오픈
cursor = conn.cursor()
sql = "select count(*) from member"
cursor.execute(sql)
#검색된 데이터 호출
count1 = cursor.fetchone()
print("개수: ",count1)
rows = cursor.fetchall()

print(rows[0][1])

conn.close()
