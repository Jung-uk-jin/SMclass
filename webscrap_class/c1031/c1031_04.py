###입력한 달 이상의 입사한 사원을 출력
import oracledb
def connects():
  user="ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외발생 : ",e)
  return conn
conn = connects()
d_day = input("숫자 입력 : ")
cursor = conn.cursor()
sql = f"select emp_name,hire_date,to_char(hire_date,'MM') from employees where to_char(hire_date,'MM') > :day"
cursor.execute(sql,day=d_day)
rows = cursor.fetchall()
for row in rows:
  print(row)