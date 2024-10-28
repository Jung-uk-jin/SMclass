students =[
  [1,'홍길동',100,100,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,100,99],
  [5,'김구',100,100,99]
]

main=input("이름 입력 : ")
for i, data in enumerate(students):
  if data[i]==main:
    del students[i]
    print(students)
  else:
    print("없음")



# all_list=[
#   [1,'홍길동',100],[2,'유관순',100],[3,'이순신',100]
# ]
# a=[3,'이순신',100]
# all_list.remove(a)
# print(all_list)

# b=[2,'유관순',100]
# all_list.remove(b)
# print(all_list)

# arr=[2,3,4,6,7,8,9,10]
# # 50, 100 추가
# arr.append(50)
# arr.append(100)
# print(arr)
# # 2번자리에 30 추가
# arr.insert(2,30)
# print(arr)
# # 숫자 6 삭제
# arr.remove(6)
# print(arr)
# # index0,3번 삭제
# del arr[0]
# del arr[3]
# print(arr)