fruit=[]
a=0

while True:
  #strip : 앞쪽, 뒤쪽여백 제거
  #replace(" ","") : 가운데공백 제거
  search=input("과일 입력(종료 : x) : ").replace(" ","")
  
  if(search=='x'):
    break
  else:
    if search in fruit:
      print("이미 있음")
      print("현재 리스트 : ",fruit)
    else:
      fruit.append(search)
      print("현재 리스트 : ",fruit)


#while True:
  #a+=1
  #print(a)
  #if(n==a):
  #  break

#while (a<10):
 # a+=1
 # print(a)