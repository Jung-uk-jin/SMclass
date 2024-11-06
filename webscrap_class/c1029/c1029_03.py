import oracledb
## sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
## sql창이 열림
cursor = conn.cursor()
# sql작성,실행
# sql문 안에 변수를 넣는 법
#1. f"{변수명}"사용 , 2. :변수명 사용 
# 3. cursor.execute(sql,sql문에 쓴 변수명 = 파이썬에서 선언한 변수명)
#이후 sql문에 입력한 파이선 변수 앞에 : 붙힘
# excute뒤에는 dict,list,tuple타입만 가능
num = input("숫자를 입력하시오 : ")
num2 = input("숫자를 입력하시오 : ")
num3 = input("숫자를 입력하시오 : ")

sql = f"select * from students where no = {num} or no = {num2} or no = {num}"
cursor.execute(sql)
# 데이터 가져오기 - fetchone():1개,fetchmany(10):숫자만큼,fetchall():모든것
rows = cursor.fetchall()
title=['번호','이름','      국어','영어','수학','총점','평균','등수','등록일']
for tit in title:
  print(tit,end="\t")
print()
print("-"*80)
for row in rows:
  for i,r in enumerate(row):
    if i==1:
      print(f"{r:10s}",end="\t")
      continue # 이후 아래의 코드 실행 x => 다음 반복으로 넘어감
    if i==6:
      print(f"{r:.2f}",end="\t")
      continue
    if i==8:
      print(r.strftime("%Y-%m-%d"),end="\t")
      continue
    print(r,end="\t")
  print()