students =[
  [1,'홍길동',100,100,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99]
]

ss=[4,'강감찬',100,100,99]

students.append(ss)
print(students)
for i,data in enumerate(students):
  print(i, " : ",students)
  del students[i]

print(students)

# for i in students:
#   if i[1]=='이순신':
#     students.remove(i)
#     print(students)


# print(students) # 한번에 출력

# for i in students:
#   print(students[1])