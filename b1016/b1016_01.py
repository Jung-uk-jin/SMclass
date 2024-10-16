#절대경로 사용
# f=open('c:/aaa/a.txt','r',encoding='UTF-8')
# r= 파일읽기 , 경로에 파일이 없으면 에러

#파일 이어쓰기 - a
while True:
   data=input("저장하려는 글 입력 : ")
   f = open("aa.txt" ,"a", encoding="UTF-8")
   f.write(data+"\n")
   f.close()

# # w = 파일쓰기
# while True:
#   data=input("저장하려는 글 입력 : ")
#   f = open("aa.txt" ,"w", encoding="UTF-8")
#   f.write(data)
#   f.close()


##파일 쓰기
#f=open('aa.txt','w',encoding='UTF-8')
#f.write("안녕하세요1\n")
#f.write("안녕하세요2\n")
#f.write("안녕하세요3\n")
#f.close()


## 파일 읽기
#f=open('b.txt','r',encoding='UTF-8')
#for line in f:
#  print(line)

#f.close()

# #파일 리스트로 읽기
# f=open('b.txt','r',encoding='UTF-8')
# lines = f.readlines()
# print(lines)
# print(type(lines))
# f.close()

# f=open('b.txt','r',encoding='UTF-8')
# while True:
#   line = f.readline()
#   if not line: break
#   print(line.strip()) #줄바꿈 생략
# f.close()