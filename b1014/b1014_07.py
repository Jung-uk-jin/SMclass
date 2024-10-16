stu_title=['국어','영어','수학']
students = {
    '국어': 90,
    '수학': 85,
    '영어': 88
}

def s_modify(choice):
  print("{} 점수 : {} ".format(stu_title[choice-1], students[stu_title[choice-1]]))
  students[stu_title[choice-1]] = int(input("변경 {} 점수 입력 : ".format(stu_title[choice-1])))

print("[점수수정]")
print("1. 국어")
print("2. 영어")
print("3. 수학")
choice = int(input("수정하려는 과목 선택 : "))
if choice==1:
  s_modify(choice)

elif choice==2:
  s_modify(choice)

elif choice==3:
  s_modify(choice)

students["총점"] = students["국어"] + students["수학"] + students["영어"]  
print("변경 : ",students)
