stu_title=['번호', '이름', '국어', '수학', '영어', '과학' , '총점' ,'평균', '등수'] 
stu_datas=[
  [1,'홍길동',100,100,100,99],
  [2,'유관순',100,99,98,99],
  [3,'이순신',100,100,90,99],
  [4,'김구',85,100,90,99],
  [5,'김유신',100,100,100,100],
]


for s_t in stu_title:
  print("{}".format(s_t),end='\t')
print()
print("*"*60)

for s in stu_datas:
  s.append(s[2]+s[3]+s[4]+s[5])
  s.append((s[2]+s[3]+s[4]+s[5])/4)
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7]))