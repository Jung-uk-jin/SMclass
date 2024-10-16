def plus(n1,n2):
  return n1+n2

a = int(input("숫자 1 입력 : "))
b = int(input("숫자 2 입력 : "))

print(plus(a,b))

# def num_sum(st,end):
#   sum=0
#   for i in range(st, end+1):
#     sum+=i
#   return sum
# # 두 수 를 입력받아 그 사이의 숫자값

# total=0
# print(f"2~50까지 합 : {num_sum(2,50):,d}")
# print("3~7까지 합 : ",num_sum(3,7))
# print("5~50까지 합 : ",num_sum(5,50))
# total = num_sum(2,50) + num_sum(3,7) + num_sum(5,50)
# print(total)