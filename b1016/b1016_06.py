import os

#os.path.exists() : 현재 폴더가 존재하는지 확인
#mkdir : 현재 폴더만 생성
#makedirs : 현재폴더, 하위폴더까지 생성
if not os.path.exists("c:ccc/bbb"):
  os.makedirs("c:ccc/bbb")

f=open("c:/bbb/c.txt","w",encoding="utf-8")
f.write("안녕하세요")
f.close()