#클래스 
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] 
s_t=['no','name','kor','eng','math','total','avg','rank']
stuNo
#class로 변경
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
print("[학생성적출력]")
for st in s_title:
  print(st,end="\t")
print()
print("-"*60)
for s in students:
  for i in range(len(s_t)):
   print(f"{s[s_t[i]]}",end="\t" )
  print()
#입력 함수
def chg(no,name,kor,eng,math,total,avg,rank):
  return { "no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"avg":avg,"rank":rank }

print("[ 학생성적 입력 ]")
    # 학생성적 직접 입력
no = stuNo + 1  # 리스트 - 학생수
name = input(f"{no}번째 학생 이름을 입력하세요.(0.이전화면) >>")
if name == "0":
  print("성적입력을 취소합니다.")
  print()
kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
total = kor+eng+math
avg = total/3
rank = 0
ss = { "no":no,"name":name,"kor":kor,"eng":eng,
      "math":math,"total":total,"avg":avg,"rank":rank }
students.append(ss)



