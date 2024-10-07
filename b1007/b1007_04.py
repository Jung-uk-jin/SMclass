import random
#1번 ~25번 까지 사이의 랜덤숫자 생성
# random.random()
# a = random.randint(1,25)
# print(a)
a_list=[]
#1~25까지 랜덤 숫자 입력 및 중복 제거
# for i in range(25):
#   a = random.randint(1,25)
#   if a not in a_list:
#     a_list.append(a)
  
# print(a_list)
# print(len(a_list))
# 1~25까지 리스트에 중복되는 숫자가 없을 때 까지 무한 출력 및 반복된 횟수 출력
# cnt=0
# while True:
#   a = random.randint(1,25)
#   cnt+=1
#   if len(a_list)==25:
#     break
#   if a not in a_list:
#     a_list.append(a)

  
# print(a_list)
# print(len(a_list))
# print(cnt)

# 1~25까지 랜덤 배치 - random.sample() 증복가능

for i in range(25):
  a_list.append(i+1)
b_list = random.choices(a_list,k=25)
print(b_list)
# 1~25까지 랜덤 배치 - random.sample() 증복안됨

b_list=random.sample(a_list,25)
print(b_list)