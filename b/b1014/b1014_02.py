def operate(cnt):
   for i in range(cnt):
      print("한국어 인사 : 안녕하세요")

while True:
  print("[외국어 인사]")
  print("1. 영어 인사")
  print("2. 일본어 인사")
  print("3. 중국어 인사")
  print("4. 프랑스 인사")
  a= int(input("원하는 번호 입력 : "))
  cnt = int(input("반복 획수 입력 : "))
  if a==1:
    operate(cnt)
    print("영어 인사 : 헬로, (Hello)")
  elif a==2:
    operate(cnt)
    print("일본어 인사 : 오하이요, (Ohayo)")
  elif a==3:
    operate(cnt)
    print("중국어 인사 : 니하오,(Ni Hao)")
  elif a==4:
    operate(cnt)
    print("프랑스 인사 : 봉주르, (Bonjour)")