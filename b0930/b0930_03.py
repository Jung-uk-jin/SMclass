print("출력")

print("""\
      1.배우 이시영이 독도에서 찍은 사진에 일부 일본 네티즌들이 악플 테러를 했다.이시
      영은 지난 26일 자신의 인스타그램에 ‘짧고 굵게 다녀온 독도’라는 제목의 글을 올리고 
      독도에서 태극기를 들고 있는 사진과 영상을 게재했다.""")

name="홍길동"
num=100
num2=100
num3=99
print("%s 합계 : %d" %(name, num+num2+num3))

print("{} 합계 : {}".format(name,num+num2+num3))
print("%s 합계 : %.2f" % (name,(num+num2+num3)/3))
print("{} 합계 : {:.2f}".format(name,(num+num2+num3)/3))

print("{:.2f}" .format(12.12345))
print("{:.2f}" .format(456.78940))
print("{:.2f}" .format(2.2525252))

print("\"\"")
print("안녕\n하세요")
print("안녕\t하세요")



print("{} 평균: {:.2f}".format("홍길동",(100+100+99)/3) )
name="홍길동"
avg="{:.2f}".format(99.6666667)
print(f"{name} 평균 : {avg}")

a=1.12345
print(f"소수점 2자리 출력 : {a:.2f}")