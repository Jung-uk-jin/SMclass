fruit="사과,배,딸기,포도,복숭아,배,사과,배,딸기"

fruits=fruit.split(",")
print(fruits)
print("전체 개수 : ",len(fruits))
name=input("과일 입력 : ")
for idx,f in enumerate(fruits):
  if f==name:
    print("해당 위치 : ",idx)
    
# print(fruit.find("딸기",6))
# print(fruit.find("배",3+1))
# print(fruit.find("배",fruit.find(fruit.find("배",0)+1)+1))


