students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강홍찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구길","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

while True:
  flag=0
  name = input("조회할 이름 입력 : ")
  sArr=[]

  for idx,s in enumerate(students):
    if s['name'].find(name)!=-1:
      # print(f"{idx+1}번째 {name}학생 찾음",s['name'])
      sArr.append(s)
      flag=1
  if flag==0:
    print("찾지 못함")
  else:
    print(f"{name}이름으로 {len(sArr)}명이 검색되었습니다")
    # stu_output(s_title,sArr)