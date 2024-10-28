import random

#랜덤 숫자 : 1~100
random.randint(1,100)

#10번 도전에서 랜덤값 찾기
num=random.randint(1,100)
i=0
while(i<10):
  search=int(input("{} 번째 도전 : 숫자를 입력하시오 :: ".format(i+1)))
  if search>num:
    print("입력된 값이 더 큽니다")
  elif search<num:
    print("입력된 값이 더 작습니다")
  else:
    print("정답입니다! 랜덤 숫자 : {}".format(num))
    break
  i+=1
if search!=num:
  print("도전에 실패했습니다. 랜덤숫자 : {}".format(num))
