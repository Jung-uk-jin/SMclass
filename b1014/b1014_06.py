import random
fName = {"바나나", "오렌지","체리", "파인애플", "코코넛"}
fruit = {"바나나" : "banana", "오렌지" : "orange", "체리" : 'cherry', "파인애플" : "pineapple", "코코넛" : "coconut"}


re_fName = random.sample(fName,5)
for i in re_fName:
  search=input(f"{i}의 영문을 입력 : ")
  if fruit[i]==search:
    print("정답")
  else:
    print("오답")



