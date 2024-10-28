student=[]
no=1

while True:
  print("학생성적프로그램")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("0. 종료")
  
  choice=int(input("번호를 입력하시오 : "))
  if choice==1:
    while True:
      name=input("이름을 입력하시오(0 입력시 종료) : ")
      if name=="0":
        break
      kor= int(input("국어 점수 입력 : "))
      eng= int(input("영어 점수 입력 : "))
      mat= int(input("수학 점수 입력 : "))
      sum=kor+eng+mat
      avg=sum/3
      s=[no, name, kor, eng, mat, sum, avg]
      student.append(s)
      print(f"{no} 이름 {name} 국어 {kor} 영어 {eng} 수학 {mat} 합계 {sum} 평균 {avg:.2f}" )
      no+=1
  elif choice==2:
    for s in student:
      print(f" 번호 {s[0]}, 이름 {s[1]}, 국어 {s[2]}, 영어 {s[3]}, 수학 {s[4]}, 합계 {s[5]},평균 {s[6]:.2f}")
  elif choice==3:
     cnt=0
     choice=input("검색할 이름을 입력 : ")
     for s in student:
       if s[1]==choice:
         print(f"{choice} 학생이 있다.")
         print("1 : 국어 점수")
         print("2 : 영어 점수")
         print("3 : 수학 점수")
         print("0 : 취소")
         num=int(input("숫자 입력 : "))
         if num==1:
           print("현재 국어 점수 : ",s[2])
           s[2]=int(input("변경할 국어 점수 : "))
         elif num==2:
           print("현재 영어 점수 : ",s[3])
           s[3]=int(input("변경할 영어 점수 : "))
         elif num==3:
           print("현재 수학 점수 : ",s[4])
           s[4]=int(input("변경할 수학 점수 : "))
         elif num==0:
           print("성적 수정 취소")
           cnt=1
         if num!=0:
           s[5]=s[2]+s[3]+s[4]
           s[6]=s[5]/3
           print(f"{name} 학생의 성적이 변경")
           cnt=1
     if cnt==0:
      print("수정하고자 하는 학생이 없음")
           
  elif choice==4:
    cnt=0
    choice=input("검색할 이름을 입력 : ")
    for s in student:
      if s[1]==choice:
        print(f"{choice} 학생이 있다.")
        print(f" 번호 {s[0]}, 이름 {s[1]}, 국어 {s[2]}, 영어 {s[3]}, 수학 {s[4]}, 합계 {s[5]},평균 {s[6]:.2f}")
        cnt=1
    if cnt==0:
      print("학생이 없음")
  
  elif choice==5:
    cnt=0
    choice=input("검색할 이름을 입력 : ")
    for idx,s in enumerate(student):
      if s[1]==choice:
        bool = input(f"{name} 학생 성적을 삭제하시겠습니까?( T: 삭제 F 취소)")
        if bool=="T":
          del student[idx]
          print("삭제되었습니다")
        elif bool =='F':
          print("취소되었습니다")
          break
        cnt=1
    if cnt==0:
      print("학생이 없다 ")

  elif choice==6:
    for s in student:
      for ss in student:
        print()
  elif choice==0:
    break
    
