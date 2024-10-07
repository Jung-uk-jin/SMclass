student=[]
choice=0
no=0; name=""; kor=0; eng=0; mat=0; sum=0; avg=0; rank=0
stNo= len(student) #학생 번호
temp=0
count=0
s_title=['번호','이름','국어','영어','수학','합계','평균','등수']
while True:
  print("[학생성적 프로그램]")
  print("-"*60)
  print("1.학생성적입력")
  print("2.학생성적출력")
  print("3.학생성적수정")
  print("4.학생성적검색")
  print("5.학생성적삭제")
  print("6.등수처리")
  print("0.종료")
  print("-"*60)
  choice = int(input("원하는 번호를 입력하시오 >>"))
  if choice==1:
    print("[학생성적입력]")
    no = stNo + 1
    name=input(f"{no}번째 헉생 이름을 입력하시오 (0 : 취소): ")
    if name==0:
      print("성적 입력 취소")
      print()
      continue
    kor=int(input("국어점수 입력 : "))
    eng=int(input("영어점수 입력 : "))
    mat=int(input("수학점수 입력 : "))
    total=kor+eng+mat
    avg=total/3
    rank=0
    student.append([no,name,kor,eng,mat,sum,avg,[rank]])
    stNo+=1
    print(f"{name}학생 정보가 저장되었습니다")
  elif choice ==2:
    print("[학생성적출력]")
    for st in s_title:
      print(f"{st}\t",end="")
    print()
    print("-"*60)
    for s in student:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t")
      print()
  elif choice ==3:
    print("[학생성적수정]")
  elif choice ==4:
    print("[학생성적검색]")
    name==input("찾고자 하는 학생의 이름 검색 : ")
    for s in student:
      if s[1]==name:
        print(f"{name}학생을 찾았습니다")
        for st in s_title:
          print(f"{st}\t",end="")
        print()
        print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\t")
        print()
  elif choice ==5:
    print("[학생성적삭제]")
  elif choice ==6:
    print("[등수처리]")
  elif choice==0:
    print("[프로그램 종료]")
    break
