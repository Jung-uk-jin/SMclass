#리스트 함수
a=[1,2,3,4,5,60,70]
a.append(100)
a.insert(0,200)
a.pop(2)
a.remove(3)
a.clear()
print(a)
# remove clear




# #리스트 삭제
# a_list=[1,2,3,4,5]
# a_list=[] # 전체 삭제
# del(a_list) # 변수까지 삭제
# # del a_list[0]
# print(a_list)

# #리스트 수정 방법
# a_list=[1,2,3,4,5,6,7]
# a_list[3]=50
# a_list[1:2]=[20,30]
# a_list[4]=[10,20] #리스트안에 ㅣ리스트
# print(a_list)


# a_list=[1,2,3,4,5]
# b_list=[50,100]
# print(a_list[0:3])
# print(a_list[2:4])
# print(a_list[:3])
# print(a_list[3:])
# print(a_list+b_list)
# print(b_list*3)
# print(a_list[::-1])
# print(a_list[::-2])

#얕은복사 깊은 복사
# a_list=[1,2,3,4,5]
# b_list = a_list # 얕은복사 , b값 변경
# a_list[0]=100
# print(a_list)
# print(b_list)
# b_list=a_list[:] # 깊은 복사, 값 변경 x
# a_list[0]=100
# print(a_list)
# print(b_list)

# a_list=[1,2,3,0,"안녕",True,False]
# b_list=a_list[::-1] # 역순출력
# print(a_list)
# print(b_list)
# print(a_list[-3])

# #순차적 출력
# for i in a_list:
#   print(i,end=" ")

# # 역순출력
# print("\n")
# for i in range(len(a_list)):
#   print(a_list[-(i+1)],end=" ")

# a_list=[]
# for i in range(100):
#   #i = int(input(f"{i+1}번째 숫자 입력  : "))
#   a_list.append(i)
#   print(i, end="\t")

# list=[]
# sum=0
# for i in range(7):
#   i=int(input(f"{i+1}번째 숫자 입력 : "))
#   list.append(i)
#   sum+=i
# print(sum)
# for idx,a in enumerate(list):
#   a=int(input("숫자 입력"))
#   sum+=a
# print(sum)