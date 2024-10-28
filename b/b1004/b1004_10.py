student=[]
no=1

while True:
  print("학생성적프로그램")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("0. 종료")

  choice=int(input("원하는 번호 입력 : "))
  if choice==1:
    name=input("{}번째 이름을 입력하시오 :".format(no))
    kor=int(input("국어 점수 입력 : "))
    eng=int(input("영어 점수 입력 : "))
    mat=int(input("수학 점수 입력 : "))
    # print(f" 번호 {no}, 이름 {name}, 국어 {kor}, 영어 {eng}, 수학 {mat}, 합계 {kor+eng+mat},평균 {(kor+eng+mat)/3:.2f}")
    s=[no,name,kor,eng,mat,kor+eng+mat,(kor+eng+mat)/3]
    student.append(s)
    print("입력되었습니다")
    no+=1
  elif choice==2:
    for s in student:
      print(s)
  
  elif choice==3:
    name=input("학생의 이름을 입력하세요 : ")
    count=0
    for s in student:
      if s[1]==name:
        print(f"{name} 학생을 찾았습니다")
        print("과목 선택")
        print("1. 국어 점수")
        print("2. 영어 점수")
        print("3. 수학 점수")
        print("0. 수정 안함")
        choice = int(input("원하는 번호를 입력 : "))
        if choice== 1:
          print("현재 국어 점수 : ",s[2])
          s[2]=int(input("변경할 국어 점수 입력 : "))
        elif choice==2:
          print("현재 영어 점수 : ",s[3])
          s[3]=int(input("변경할 국어 점수 입력 : "))
        elif choice==3:
          print("현재 수학 점수 : ",s[4])
          s[4]=int(input("변경할 국어 점수 입력 : "))
        elif choice==0:
          print("성적 수정 취소")
          count=1
        if choice!=0:
          s[5]=s[2]+s[3]+s[4]
          s[6]=s[5]/3
          print(f"{name} 학생의 성적이 변경")
          count=1
      if count==0:
        print("수정하고자 하는 학생이 없음")
  elif choice==4:
    name=input("학생의 이름을 입력하세요 : ")
    count=0
    for s in student:
      if s[1]==name:
        print(f"{name} 학생을 찾았습니다")
        print(f" 번호 {s[0]}, 이름 {s[1]}, 국어 {s[2]}, 영어 {s[3]}, 수학 {s[4]}, 합계 {s[5]},평균 {s[6]}")
        count=1
    if(count==0):
      print("학생이 없음")
  elif choice==0:
    print("종료합니다")
    break