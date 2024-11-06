import oracledb
def connection(): # 에외처리 
  try:
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    print("db연결 : ",conn.version)
  except Exception as e:
    print("예외 발생 : ",e)
  return conn
num1 = int(input("최소 범위 입력 : "))
num2 = int(input("최대 범위 입력 : "))
conn=connection()
cursor = conn.cursor()
# search = input("검색할 이름 입력 : ")
# search = input("번호 검색 : ")
# sql = f"select employee_id, emp_name from employees where employee_id >= {search}"
# sql = f"select employee_id, emp_name,salary from employees where salary>=4000 and salary <=8000" 
sql = f"select employee_id, emp_name,salary from employees where salary>={num1} and salary<={num2} order by salary asc" 
cursor.execute(sql)
title=['employee_id', 'emp_name','salary'] # 제목 : 
a_list=[] # : 내용
rows = cursor.fetchall()
for row in rows:
  a_list.append(dict(zip(title,row))) #딕셔너리로 묶임
print(a_list)
cursor.close()


