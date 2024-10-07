#for문 출력 
for k in range(2,10):
  print(f"{k}단",end="\t")
print()
for i in range(2,10):
  for j in range(1,10):
    print(f"{i} x {j} = {i*j}",end="\t")
  print()


#000
#001
#...999
# for 문 3번
# for i in range(10):
#   for j in range(10):
#     for k in range(10):
#       print(f"{i}{j}{k}")
# # for 문 1번
# for i in range(1000):
#   print(f"{i:03d}")

# #구구단 입력한 단까지 출력
# a=int(input("단을 입력하시오 :"))
# if a<=1:
#   print("2단보다 작습니다")
# for i in range(2,a+1):
#   print(f"{i}단")
#   for j in range(1,10):
#     print(f"{i} * {j} = {i*j}")