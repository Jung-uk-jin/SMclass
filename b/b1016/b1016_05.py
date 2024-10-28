#
#  #파일 (바이너리 파일) 읽기
f=open('1.jpg',"rb")
fData = f.read()
f.close()
print("파일 읽기 성공")


#
#  #파일 (바이너리 파일) 읽기
# f=open('1.jpg',"rb")
# fData = f.read()
# f.close()
# print("파일 읽기 성공")



# # txt파일의 내용 복사 f-> ff
# f=open("students.txt","r",encoding='utf-8')
# ff=open("students2.txt","w",encoding="utf-8")
# while True:
#   line = f.readline()
#   if not line: break
#   ff.write(line)
#   print(line.strip())
# f.close()
# ff.close()

