class student:
  cnt=0
  def __init__(self,no,name,kor,eng,math):
    student.cnt+=1
    self.no=student.cnt
    self.name=name
    self.kor=kor
    self.eng=eng
    self.math=math
    self.total=kor+eng+math
    self.avg=(kor+eng+math)/3
    self.rank=0

  def print(self):
    return { "no":self.no,"name":self.name,"kor":self.kor,"eng":self.eng,
            "math":self.math,"total":self.total,"avg":self.avg,"rank":self.rank }
  
  def __str__(self):
    return 
  
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] 
s_t=['no','name','kor','eng','math','total','avg','rank']

students=[]
while True:
  print("[학생성적프로그램]")
  print("1.학생성적입력")
  print("2.학생성적출력")
  choice = int(input("원하는 번호 입력 : "))
  if choice==1:
    print("[학생성적입력]")
    name=input("이름 입력 : ")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]}점수 입력 : ")))
    s1=student(name, *score) # 전개연산자
    # s1=student(name,score[0],score[1],score[2])
    students.append(s1.print())
    print(students)
s1=student(1,"홍길동",100,100,99)
print(s1.print())
s2=student(2,"유관순",100,90,90)
print(s2.print())