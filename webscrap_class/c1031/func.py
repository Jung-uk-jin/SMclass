import oracledb
import random
import smtplib
from email.mime.text import MIMEText
## db연결 함수선언
def connects():
  user="ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외처리 :",e)
  return conn
# 랜덤비밀번호 생성 함수선언
def random_pw():
  # 랜덤
  a = random.randrange(0,10000) #0-9999
  ran_num = f"{a:04}"   #5412,0124,0001... 숫자형
  print("랜덤번호 : ",ran_num)
  return ran_num
# 메일발송 함수선언
def emailSend(email):
  #email 발송
  smtpName = "smtp.naver.com"
  smtpPort = 587
  sendEmail = "onulee@naver.com"
  pw = "G5VCZR3EGZMZ"
  recvEmail = email
  title ="[ 메일발송 ] 임시비밀번호 안내"
  ##### 랜덤비밀번호
  ran_num = random_pw()
  # 설정
  content = f"임시비밀번호 : {ran_num}"
  print(content)
  msg = MIMEText(content)
  msg['Subject'] = title
  msg['From'] = sendEmail
  msg['To'] = recvEmail
  # 서버이름,서버포트
  s = smtplib.SMTP(smtpName,smtpPort)
  s.starttls()
  s.login(sendEmail,pw)
  s.sendmail(sendEmail,recvEmail,msg.as_string())
  s.quit()
  # 메일발송완료
  print("메일이 발송되었습니다.")
  return ran_num