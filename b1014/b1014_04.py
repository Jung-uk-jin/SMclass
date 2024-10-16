def calc(n1,n2,op):
  if op=="+":
    return n1+n2
  elif op=="-":
    return n1-n2
  elif op=="*":
    return n1*n2
  elif op=="/":
    return n1/n2

a = int(input("숫자 1 입력 : "))
b = int(input("숫자 2 입력 : "))
op = input("+, -, *, / 중 하나를 선택 : ")

print("결과 : ", calc(a,b,op))

