import oracledb

def connects():
  user = "ora_user"
  password="1111"
  dsn = "localhost:1521/xe"
  try: conn=oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외처리 : ",e)
  return conn

conn=connects()
cursor=conn.cursor()
sql="select * from chartable"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
  print(f"합 : {row[1] + row[2]}")
  print(row)
