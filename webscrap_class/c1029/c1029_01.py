import oracledb
#developer 실행
conn = oracledb.connect(user="ora_user",password="1111",dsn='localhost:1521/xe')

#sql 실행창 오픈
cursor = conn.cursor()
#sql 작성, 실행
sql = "select * from students"
cursor.execute(sql)
#검색된 데이터 호출 # fecthone()1개 fetchmany(n)n개만큼 fetchall()모든것
rows = cursor.fetchall()
title=['번호','이름','국어','영어','수학','총점','평균','등수','등록일']
for tit in title:
  print(tit,end="\t")
print()
print("-"*80)
for row in rows:
  for i,r in enumerate(row):
    if i==1:
      print(f"{r:12}",end="\t")
    if i==6:
      print(f"{r:.2f}",end="\t")
      continue
    if i==8:
      print(r.strftime("%Y-%m-%d"),end="\t")
      continue
    print(r,end="\t")
  print()
conn.close()