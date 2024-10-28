#10은 2의 배수입니다
a=10
b=2

print(a,b)
print("%d * %d = %d" %(a,b,a*b)) 
name="홍길동"
kor=100
eng=100
mat=99
#%d 정수 #f 실수 %c 한글자 %s 두글자 이상 %x 16진수 %o 8진수
print("%s 총합 : %d , 평균 %.2f" %(name, (kor+mat+eng), ((kor+mat+eng)/3))) 

#출력 자리수
print("%d" %b)
print("%5d" %b)
print("%05d" %b)

#001 010 100.00 3번 프린트를 사용하여 출력
num=1
num2=10
num3=100
print("%03d" %num)
print("%03d" %num2)
print("%.2f" %num3)

print("%5d" %(-10))

#print 1, 쉼표, format f
# print(a,"은" ,b,"의 배수입니다")
# print("%d는 %d의 배수입니다." %(a,b))
# print("{}은 {}의 배수입니다".format(a,b) )
# print(f"{a}은 {b}의 배수입니다")

#quiz
print("%.2f" %758.12345678)
print("%010.02f" %25.05)
print("%d %f %s" %(150.15, 150.15 ,150.15))
print("*"*10)
print("언뇽"+"hello")
print("%5.1f" %(12345789.12) )
