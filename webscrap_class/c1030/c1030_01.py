import random
import oracledb
# email 발송관련
import smtplib
from email.mime.text import MIMEText

def connects():
  user="ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외발생 : ",e)
  return conn
while True:
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 찾기")
  print("3. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요.>> ")
  if choice == "1":
    print("[ 로그인 ]")
    user_id = input("아이디를 입력하세요.>> ")
    user_pw = input("패스워드를 입력하세요.>> ")
    # db접속
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id and pw=:pw"
    cursor.execute(sql,id=user_id,pw=user_pw)
    row = cursor.fetchone() # None
    print(row)
    if row != None:
      print(f"로그인 성공! {row[2]} 님 환영합니다.")
    else:
      print("아이디 또는 패스워드가 일치하지 않습니다. 정확히 입력하세요!! ")
    cursor.close()
    # 오라클db에 접속해서 member테이블에서 검색 가져옴.
    # if user_id == 'aaa' and user_pw == "1111":
    #   print("로그인 성공")
    # else:
    #   print("로그인 실패")
    #   continue
    print("[ 학생성적 프로그램에 접속합니다. ]")
    ### 프로그램 구현 ###
  elif choice == "2":
    print("[ 비밀번호 찾기 ]")
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
    print("변경된 번호 : ",user_pw)
    print("메일 보내기 성공")
    cursor.close()
  elif choice == "3":
    pass
  elif choice == "0":
    print("프로그램 종료합니다.")
    break