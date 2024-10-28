import random




#1~25까지의 랜덤숫자 25개를 중복없이 추출해서 (5,5) 2차원 리스트에 입력 후 출력
 

a_list=[]
for i in range(25):
  a_list.append(i+1)
random.shuffle(a_list)
print(a_list)
b=[]
for i in range(0,len(a_list),5):
  b.append(a_list[i:i+5])

print(b)

b_list=[]
for i in range(0,len(a_list),5):
  b_list.append(a_list[i:i+5])

while True:
  for i in range(5):
   for j in range(5):
     print(b_list[i][j],end='\t')
   print()
  input1= input("좌표를 입력하시오 ")
  input2=input1.split(",")
  print(input2)
  print(f"{input1} 좌표의 값은 : ",b_list[int(input2[0])][int(input2[1])])

  

#2.
# while len(a_list)<25:
#   num=random.randint(1,25)
#   if num not in a_list:
#     a_list.append(num)

# for i in range(5):
#   a=[]
# b=[]
#   for j in range(5):
#     a.append(a_list[5*i+j])
#   b.append(a)
# print(b)


