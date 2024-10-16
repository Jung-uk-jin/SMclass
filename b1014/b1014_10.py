students = [
  {"no":1,"name":"홍길동"},
  {"no":2,"name":"유관순"},
  {"no":3,"name":"이순신"}
]
stNo = len(students)
def stu_input(stNo,students):
  while True:
    no = stNo +1
    print("no :", no)
    name = input(f"{no}번쨰 학생 이름 입력 : ")
    if name==0:
      break
    students.append({"no": no, "name": name})
    print(students)
    stNo+=1
  return stNo

stu_input(stNo,students)
print("stNo : ", stNo)
print(students)