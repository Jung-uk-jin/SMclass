s_list=[]
no=1
while True:
  name=input("이름 입력 (0입력시 종료) : ")
  kor=int(input("국어 점수 입력 :"))
  emg=int(input("영어 점수 입력 :"))
  mat=int(input("수학 점수 입력 : "))

  if name==0:
    break
  print(f"{no}, {name}, {kor}, {emg}, {mat}, {kor+emg+mat}, {(kor+emg+mat)/3:.2f}")

# # 두 수를 입력받아 더하기 빼기 곱하기 나누기 출력

# while True:
#   a=int(input("첫번쨰 숫자 입력 : "))
#   b=int(input("두번쨰 숫자 입력 (종료 : 0)"))
#   if b==0:
#     break
#   print("두 수의 사칙연산")
#   print("1 더하기")
#   print("2 빼기")
#   print("3 곱하기")
#   print("4 나누기")

#   choice=int(input("원하는 번호 입력 : "))
#   if choice==1:
#     print("결과 : {} + {} = {}".format(a,b,a+b))
#   elif choice==2:
#     print("결과 : {} - {} = {}".format(a,b,a-b))
#   elif choice==3:
#     print("결과 : {} * {} = {}".format(a,b,a*b))
#   elif choice==4:
#     print("결과 : {} / {} = {}".format(a,b,a/b))
#   else:
#     print("번호에 맞게 입력하십시오")

# i=1
# j=1
# while i<10:
#   while j<10:
#     if j%2!=0:
#       print(i,j)


# i=0 
# j=0
# while i<10:
#   print("번호 1:",i)
#   while j<10:
#     if j==5:
#       break
#     print("번호2",j)




# sum=0
# while True:
#   num=int(input("숫자 입력 : "))
#   if num==0:
#     break
#   sum+=num
# print(sum)

# i=1
# j=1
# while(i<10):
#   print(f"{i}단")
#   while(j<10):
#     print("{} * {} = {}".format(i,j,i*j))
#     j+=1
#   j=1
#   i+=1

# i=0
# while(i<10):
#   print(i)
#   i+=1