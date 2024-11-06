import random
import oracledb
# email 발송관련
import smtplib
from email.mime.text import MIMEText

# 메일발송 완료
def connects():
  user="ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외발생 : ",e)
  return conn
conn = connects()
user_id = input("아이디를 입력하세요.>> ")
user_pw = random.randrange(0,10000)
cursor = conn.cursor()
#데이터 수정
sql = "update member set pw=:pw where id=:id"
cursor.execute(sql,id=user_id,pw=user_pw)
conn.commit()
print("비번 변경됨")

smtpName = "smtp.naver.com"
smtpPort = 587

# 자신의 네이버메일주소,pw, 받는사람이메일주소
sendEmail = "ukjin32@naver.com"
pw = "jin3272**"
recvEmail = "ukjin32@naver.com"
title = "제목 : 비밀번호 이메일보내기 안내"
content = f"""\
임시 비밀번호 발송입니다
임시 번호는 {user_pw}
"""

# 설정
msg = MIMEText(content)
msg['Subject'] = title
msg["From"] = sendEmail
msg['To'] = recvEmail
print("msg 데이터 : ",msg.as_string())

# 서버이름,서버포트
s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()
# 2단계 보안설정이 되어 있는 경우는 에러 발생
# 인증키 발급을 받아야 함.
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.quit()
print("메일 보내기 성공")
cursor.close()

# a=random.randrange(0,10000) 1690
# ran_num=f"{a:08}"
# print(ran_num)
