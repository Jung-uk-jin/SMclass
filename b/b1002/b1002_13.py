import random

aArr=[]
#10개의 랜덤숫자 출력 0~9까지

for i in range(10): # 10개 반복 // 다 들어오지 못할 수도 있음
  num=random.randint(0,9)
  if num not in aArr:
    aArr.append(num)
print(aArr)

i=0
while i<10: # 10개가 들어갈 때 까지 반복
   num=random.randint(0,9)
   if num not in aArr:
    aArr.append(num)
    i+=1

print(aArr)