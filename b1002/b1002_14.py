import random

#1~100까지 랜덤 숫자 생성
num=random.randint(1,100)
i=0
#입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다
#입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다

#while문

while i<10:
  search=input("{} 번째 숫자 입력 : ".format(i+1))
  if(int(search)>num):
    print("입력한 숫자가 더 큽니다")
  elif(int(search)<num):
    print("입력한 숫자가 더 작습니다")
  else:
    print("정답입니다!")
    break
  i=i+1
if int(search)!=num:
  print("정답을 못찾았습니다")

#FOR문

#for i in range(10):
 # search=input("{} 번째 숫자 입력 : ".format(i+1))
 # if(int(search)>num):
 #   print("입력한 숫자가 더 큽니다")
 # elif(int(search)<num):
 #   print("입력한 숫자가 더 작습니다")
 # else:
#    print("정답입니다!")
#    break
#if int(search)!=num:
#  print("정답을 못찾았습니다")