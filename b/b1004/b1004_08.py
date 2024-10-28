s_list=[]
no=1
while True:
  print("학생성적프로그램")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("0. 종료")

  choice=int(input("원하는 번호를 입력 : "))

  if choice==1:
    name=input("이름 입력 : 0은 종료 : ")
    if name==0:
      break
    kor = int(input("국어 점수 입력 : "))
    eng = int(input("영어 점수 입력 : "))
    mat = int(input("수학 점수 입력 : "))
    s=[no,name,kor,eng,mat,kor+eng+mat,(kor+eng+mat)/3]
    s_list.append(s)
    print("입력되었습니다")
  
  elif choice==2:
    print(f" 번호 {no}, 이름 {name}, 국어 {kor}, 영어 {eng}, 수학 {mat}, 합계 {kor+eng+mat},평균 {(kor+eng+mat)/3:.2f}")
    no+1

