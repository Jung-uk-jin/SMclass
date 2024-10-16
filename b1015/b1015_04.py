students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수

choice=input("번호 입력 : ")

def stu_update():
  print("< 학생성적 수정>")
  name = input("학생 이름 입력 : ")

  for s in students:
    if s['name']==name:
      print("1 국어 점수")
      print("2 영어 점수")
      print("3 수학 점수")
      choice = input("번호 입력 : ")
      if choice=="1":
        print("이전 국어 점수 : {}".format(s["kor"]))
        s["kor"]= int(input("변경 국어 점수 : "))
      elif choice=="2":
        print("이전 국어 점수 : {}".format(s["eng"]))
        s["eng"]= int(input("변경 영어 점수 : "))
      elif choice=="3":
        print("이전 국어 점수 : {}".format(s["math"]))
        s["math"]= int(input("변경 수학 점수 : "))
      
      s['total']=s['kor']+s["eng"]+s["math"]
      s['avg'] = s['total']/3
      flag =1
  if flag==0:
    print("학생 없음")
    print()

flag=0
if choice==3:
  stu_update()
    
