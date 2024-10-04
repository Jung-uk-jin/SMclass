students =[
  [1,'홍길동',100,100,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99]
]

for i in range(10): # 0부터 10이전까지 돌림 .. 0 1 2 3 4 5 6 7 8 9
  print(i)

for i in range(2,5): # 2부터 5이전까지
  print(i)

for i in range(1,10,2): # 1부터 10이전까지 ++2로 출력
  print(i)
arr=[1,3,5,9,8]
for i in arr: # 리스트의 값을 1개씩 가져와서 출력
  print(i)
for i,data in enumerate(arr) :
  print(i, ":" , data)

str="안녕하세요"
for i in str: # 문자열의 값을 1개씩 가져와서 출력
  print(i)

# s=[4,'강감찬',100,100,99]
# print(s)
# s.append(s[2]+s[3]+s[4])
# s.append((s[2]+s[3]+s[4])//3)
# print(s)

# list=[1,2,3]
# list.append(10)
# print(list)

# list.insert(2,100)
# print(list)

# del list[1]
# print(list)

# list.remove(100)
# print(list)

# str="좋은 하루되세요. 많은 행복받으세요. 많은 감사! 많은 돈."
# print(len(str))

# print(str[-5:])
# print(str[-1])