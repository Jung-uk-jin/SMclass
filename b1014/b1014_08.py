def calc():
  global sum # 글로벌 변수 
  sum=200

sum=10
calc()
print(sum)

# def cal(n1,n2):
#   s1=n1+n2
#   s2=n1-n2
#   s3=n1*n2
#   s4=n1/n2
#   s5 = [s1,s2,s3,s4]
#   return s5

# a=cal(10,5)
# print(a)

# print(1,2,3,sep=",",end="\t")
# print("안영")
# def cal(n1=10 ,n2=20):
  
#   print(n1)
#   print(n2)

# cal()
# cal(300)
# def calc(*n): # 가변매개변수
#   print(n)
#   print(len(n))

# calc(1,2,3,4,5,6)


# def cal(a,b,c):
#   print(a+b+c)
#   print(a-b-c)
#   print(a*b*c)
#   print("{:.2f}".format(a/b/c))
# def cal(a,b):
#   print(a+b)
#   print(a-b)
#   print(a*b)
#   print(a/b)

# numstr = input("3개 숫자 입력 :(12,21,3) : ")

# numstr2=numstr.split(",")

# a=int(numstr2[0])
# b=int(numstr2[1])
# c=int(numstr2[2])

# cal(a,b,c)




# numstr=input("3개 숫자 입력 : (12,5) : ")
# numstr2=numstr.split(",")

# a=int(numstr2[0])
# b=int(numstr2[1])

# cal(a,b)

# for i in range(len(a)):
  # print(a[i]+b[i])
  # print(a[i]-b[i])
  # print(a[i]*b[i])
  # print(a[i]/b[i])
  # print("----------")