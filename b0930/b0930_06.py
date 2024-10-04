stu_data=['홍길동',100,100,100,99]
# for s in stu_data:
#   print(s)
stu_title=['번호', '이름', '국어', '수학', '영어', '과학' , '총점' ,'평균']
stu_datas=[
  [1,'유관순',100,100,100,99],
  [2,'이순신',100,99,98,99],
  [3,'김구',80,100,90,99],
]
for s_t in stu_title:
  print("{}".format(s_t),end='\t')
print()
print("-"*60)
for s in stu_datas:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(s[0],s[1],s[2],s[3],s[4],s[5],s[2]+s[3]+s[4]+s[5],(s[2]+s[3]+s[4]+s[5])/4))
# print((stu_datas[1][1]+stu_datas[1][2]+stu_datas[1][3]+stu_datas[1][4])/4)

#학생이름 : 홍길동 국어 100 영어 100 수학 100 과학 99
# print("학생 이름 : {}".format(stu_data[0]))
# print("국어 : {}".format(stu_data[1]))
# print("영어 : {}".format(stu_data[2]))
# print("수학 : {}".format(stu_data[3]))
# print("과학 : {}".format(stu_data[4]))
# print("합계 : {}".format(stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4]))
# print("평균 : {}".format((stu_data[1]+stu_data[2]+stu_data[3]+stu_data[4])/4))

# print()


# # 한번에 두 길이를 입력받아 삼각형의 넓이 직사각형ㅇ의 넓이를 구하시오
# l=input("2개의 길이를 한번에 입력하시오")
# print(l.split(" "))
# l_list=l.split()
# print("삼각형의 넓이 : {}".format(int(l_list[0])*int(l_list[1])/2))
# print("사각형의 넓이 : {}".format(int(l_list[0])*int(l_list[1])))

# #원의 넓이
# a=input("반지름의 길이 입력 :")
# print((int(a)**2)*3.14)