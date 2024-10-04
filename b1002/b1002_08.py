fruit="사과,배,딸기,포도,복숭아,배,사과,배,딸기"
idx=0
name=input("과일 이름 입력")
if fruit.count(name)>0:
  for i in range(fruit.count(name)):
    for i in range(idx,len(fruit)):
      print(fruit.find(name,idx))
      idx = fruit.find(name,idx)+1
      break
else:
  print("배는 없다")


# name = input("과일 이름 입력 : ")
# if name in fruit: # in 데이터가 있는지 확인
#   print("과일 있음. {}개".format(fruit.count(name))) # count 데이터의 개수 
#   print(fruit.index(name)) # find 데이터가 있는 위치, 없으면 -1
#   print(fruit.find(name)) # index 데이터가 있는 위치, 없으면 에러
# else:
#   print("없음")

# print(fruit.count('배'))
# print(fruit.count('사과'))

# fruits = ['사과,배,배,배,배,배,사과']
# print(fruits.count('배'))

# name=input("과일 입력")
# if name in fruit:
#   print("있")
# else:
#   print("없")

# if '배' in fruit:
#   print("잇")
#   sum=0
#   sum=sum+1

# else:
#   print("없")
