students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
stNo=len(students)

def stu_input(stNo, students):
  while True:
    no = stNo+1
    print(f"{no}번째")
    a=input("학생의 이름을 입력(0은 취소) : ")
    if a=="0":
      break
    b=int(input("학생의 국어 입력 : "))
    c=int(input("학생의 영어 입력 : "))
    d=int(input("학생의 수학 입력 : "))
    rank=0
    students.append({"no": no, "name": a, "kor" : b, "eng" : c, "mat" : b, "total" : b+c+d, "avg" : (b+c+d)/3, "rank" : rank})
    stNo+=1

  return stNo

stu_input(stNo, students)
print(students)