def plus(a):
  a=20
  print("지역변수 a : ",a )
  return a

a=[10,20]
a= plus(a)
print("전역변수 a :",a)