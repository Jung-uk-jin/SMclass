import random
lotto=[0]*6+[1]*3
a_list=[
  [0,1,0],
  [1,0,0],
  [0,0,1]
]
random.shuffle(lotto)
for i in range(3):

  for j in range(3):
    a_list[i][j]=lotto[3*i+j]

aa_list=[
  ["로또", "로또", "로또"],
  ["로또", "로또", "로또"],
  ["로또", "로또", "로또"],
]
while True:
  print(aa_list)
  myMoney = int(input("얼마를 투자하시겠습니다? : "))
  print("[    i,j좌표]")
  print("\t0\t1\t2\t")
  print("-"*30)
  for i in range(3):
    print(i," | ", end="\t")
    for j in range(3):
      print(a_list[i][j],end="\t")
    print() 
  
  code =  input("좌표 입력 :")
  codeArr=code.split('.')

  if a_list[int(codeArr[0])][int(codeArr[1])]==1:
    aa_list[int(codeArr[0])][int(codeArr[1])] = "당첨"
    print(f"{codeArr} 당첨금 : {myMoney*100}")
  else:
    aa_list[int(codeArr[0])][int(codeArr[0])] = "꽝"
    print(f"{codeArr} 당첨금 : {myMoney*0}")