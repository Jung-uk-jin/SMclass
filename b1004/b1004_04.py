# 두 수를 입력받아 두수까지의 합계

#1 
sum=0
a=int(input("첫번째 수 입력"))
b=int(input("두번째 수 입력"))
if a>b:
  a,b=b,a # 두개 변수 치환 // 파이선만 가능
  
for i in range(a,b+1):
  sum+=i
print(sum)
#2.
# sum=0
# max_num=0
# min_num=0
# a=int(input("첫번째 수 입력"))
# b=int(input("두번째 수 입력"))
# if a>b:
#   max_num=a
#   min_num=b
# else:
#   max_num=b
#   min_num=a
# for i in range(min_num,max_num+1):
#   sum+=i
# print(sum)
# # 1부터 100까지의 홀수 합
# sum=0
# for i in range(1,101):
#   if(i%2!=0):
#     sum+=i
# print(sum)


# # 1부터 100까지 합
# sum=0 
# for i in range(1,101):
#   sum+=i
# print(sum)

# # 0 : 안녕하세요
# # 1: 안녕하세요
# #2 : 안녕하세요
# for i in range(3):
#   print(f"{i} : 안녕하세요")

# # 1번 출력 2번 출력 3번출력
# for i in range(1,4):
#   print("안녕하세요"*i)

# #for문을 이용해서 
# for i in range(5,0,-1):
#     print("*"*i)

# for i in range(1,10,2): #(n,m,o) n부터 m-1까지 o를 증가하여 반복 
#   for j in range(1,10):
#     print("{} * {} = {}".format(i,j,i*j))

# #구구단 홀수단 출력
# for i in range(1,10):
#   if(i%2!=0):
#     print("{}단".format(i))
#     for j in range(2,10):
#       print("{} * {} = {}".format(i,j,i*j))
#     print("-"*20)

# #구구단 출력
# for i in range(2,10):
#   print("{}단".format(i))
#   for j in range(2,10):
#     print("{} * {} = {}".format(i,j,i*j))
#   print("-"*20)

## 홀수 출력
# for i in range(10):
#   if(i%2!=0):
#     print(i)

#1 부터 10까지 for문 사용
# for i in range(1,11): # (n.m) n부터 m-1까지 출력
#   print(i)