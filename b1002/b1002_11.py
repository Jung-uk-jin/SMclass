students =[
  [1,'홍길동',100,100,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

#합계 평균 추가
for s in students:
  s.append(s[2]+s[3]+s[4])
  s.append((s[2]+s[3]+s[4])//3)
print(students)
search=input("학생 이름을 입력 : ")
cnt=0  # 작성 이유 : 출력이 여러번 되지 않게 하기 위함
for s in students:
  if s[1]==search:
    print("학생 이름이 있다")
    cnt=1
    break
if cnt==0:
  print("학생 이름이 없다")
