import random
lotto=[0]*20+[1]*5
a_list=[
  [1,0,0,0,0],
  [1,0,0,0,0],
  [1,0,0,0,0],
  [1,0,0,0,0],
  [1,0,0,0,0],
]
random.shuffle(lotto)
for i in range(5):
  for j in range(5):
    a_list[i][j]=lotto[5*i+j]

aa_list=[
  ["로또", "로또", "로또","로또","로또"],
  ["로또", "로또", "로또","로또","로또"],
  ["로또", "로또", "로또","로또","로또"],
  ["로또", "로또", "로또","로또","로또"],
  ["로또", "로또", "로또","로또","로또"],
]
while True:
  print(aa_list)
