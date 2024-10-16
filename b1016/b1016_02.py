while True:
  no = input("번호를 입력하세요 ")
  if no=="0": break
  name = input("이름 입력 ")
  kor = int(input("국어 점수 입력 "))
  eng = int(input("영어 점수 입력 "))
  math = int(input("수학 점수 입력 "))
  total=kor+eng+math
  avg=total/3
  rank=0
  data = f"{no}, {name}, {kor}, {eng}, {math}, {total}, {avg}, {rank}\n"
  f=open("a.txt",'a', encoding='utf-8')
  f.write(data)
  f.close()