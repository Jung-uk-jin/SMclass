def func(num1,num2): # 함수선언
  print(num1)
  print(num2)

#함수 호출
#func(10,20)
#함수 호출시 매개변수와 변수의 개수가 같아야함
def func(*num):
  print(num)

func(10,20)
