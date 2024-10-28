import random

list1=[0]*20+[1]*5
random.shuffle(list1)
print(list1)

list2=[]
for i in range(5):
  a=[]
  for j in range(5):
    a.append(list1[5*i+j])
  list2.append(a)
print(list2)

for i in  range(5):
  for j in range(5):
    print(list2[i][j],end="\t")
  print()
num = input("좌표 입력 : ")
num2 = num.split(',')
print(f"{num} 좌표값 : {list2[int(num2[0])][int(num2[1])]}")

# for i in range(25):
#   if i<5:
#     list1.append(1)
#   else:
#     list1.append(0)
# print(list1)
