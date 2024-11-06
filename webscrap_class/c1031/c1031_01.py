import func
while True:
  # 로그인이 되어 있지 않은 상태
  print("[ 커뮤니티 ]")
  print("1.로그인")
  print("2.비밀번호 찾기")
  print("3.회원가입")
  print("4.프로그램 종료")
  choice = input("원하는 번호를 입력하세요.>> ")
  # 로그인이 되어 있는 상태
  # print("[ 학생성적 프로그램 ]")
  # print("1. 학생성적 입력")
  # print("2. 학생성적 출력")
  # print("3. 학생성적 수정")
  # print("4. 로그아웃")
  if choice == "1":
    user_id = input("아이디를 입력하세요.>> ")
    user_pw = input("패스워드를 입력하세요.>> ")
    # db접속
    conn = func.connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id and pw=:pw"
    cursor.execute(sql,id=user_id,pw=user_pw)
    row = cursor.fetchone()
    cursor.close()
    if row == None :
      print("아이디 또는 패스워드가 일치하지 않습니다. 다시 입력하세요!")
      continue
    ## 이후 프로그램 구성
    print(f"{row[2]} 님 환영합니다.")
    print()
  elif choice == "2":
    user_id = input("아이디를 입력하세요.>> ")
    # db접속
    conn = func.connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id"
    cursor.execute(sql,id=user_id)
    row = cursor.fetchone()
    if row == None:
      print("아이디가 존재하지 않습니다. 다시 입력하세요!")
      continue
    input(f"{row[0]} 아이디가 존재합니다. 메일을 보내려면 enter를 입력하세요.")
    print("이메일 : ",row[3])
    #### 이메일발송함수 호출
    ran_num = func.emailSend(row[3])
    # 임시비밀번호를 update
    sql = "update member set pw=:pw where id=:id"
    cursor.execute(sql,pw=ran_num,id=user_id)
    conn.commit()