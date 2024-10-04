import random
i=0
num=random.randint(1,100)
while i<10:
  search=input("{} 번째 숫자 입력 : ".format(i+1))
  if int(search)>num:
    print("입력 값이 더 크다")
  elif int(search)<num:
    print("입력 값이 더 작다")
  else:
    print("정답입니다!")
    break
  i+=1
if int(search)!=num:
 print("정답이 아닙니다")