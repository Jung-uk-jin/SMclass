students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #

#===========
def stu_input(stuNo):
  while True:
    no = stuNo+1
    name=input(f"{no}번째 학생 입력 (취소 0) : ")
    if name=="0":
      break
    kor = int(input("국어 점수 입력 : "))
    eng = int(input("영어 점수 입력 : "))
    math = int(input("수학 점수 입력 : "))
    total=kor+eng+math/3
    avg=total/3
    rank=0

    s = { "no":no,"name":name,"kor":kor,"eng":eng,
             "math":math,"total":total,"avg":avg,"rank":rank }
    students.append(s)
    stuNo+=1
    print(f"{name}학생 입력됨")
    print()

def stu_output(s_title,students):
  for st in s_title:
    print(st,end="\t")
  print("-"*50)
  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()

def stu_update(s_title,students):
  pass

def stu_search(s_title,students):
  choice = input("수정할 이름 검색 : ")
  chk=0
  for idx,s in enumerate(students):
    if choice == s['name']:
      print(f"{choice} 학생 찾음")

#==============
while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = int(input("원하는 번호를 입력하세요.(0.종료)>> "))

  if choice==1:
    stu_input(stuNo)
  elif choice==2:
    stu_output(s_title,students)
  elif choice==3:
    stu_update(s_title,students)
  elif choice==4:
    stu_search(s_title,students)
  elif choice==5:
    pass
  elif choice==6:
    pass
  elif choice==7:
    pass
  elif choice==0:
    break
