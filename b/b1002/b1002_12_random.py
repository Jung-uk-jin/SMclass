import random
#랜덤 숫자 생성 = random
#random() : 0<=x<1 0~1사이에 있는 실수값 
print(random.random()+1)
#0~9까지 출력
print(int(random.random()*10))
#1~10
print(int(random.random()*10)+1)

# 랜덤 int 출력 randint(x,y) x부터 y까지 (y포함)
print(random.randint(1,10))

#랜덤 범위 출력 randrange(1,3) 3포함 안됨
print(random.randrange(1,3))

#리스트에서  랜덤 출력
a=[1,4,5,6,7]
print(random.choice(a))

#리스트에서 여러개 랜덤 출력 ( 중복가능)
print(random.choices(a,k=2))

#리스트에서 여러개 랜덤 출력 ( 중복 불가)
print(random.sample(a,2))
