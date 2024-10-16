print("숫자 입력 : ")
num = int(input("숫자만 입력 가능 : "))
if num.isdigit():
  num=int(num)
  print("입력된 숫자 : ",num)
else:
  print("변환 안됨")