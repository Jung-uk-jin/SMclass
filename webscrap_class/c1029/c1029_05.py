# a=1
# b=2

# a_list = [a,b]
# print(a_list)

# print(type(a_list))
# a_tuple=(a,b)
# print(a_tuple)
# b_tuple = (a,)
# print(b_tuple)
# print(type(b_tuple))

# 튜플을 한개만 지정할때에는 ()변수뒤에 쉼표 추가

# name = "홍길동"
# print("my name is {}".format(name))

title = ['e_id', 192, 'edaoa']
a=[196,'alem tn', 3022.0]
aa=[
  (196, 'Alana Walsh', 3100.0),
  (125, 'Julia Nayer', 3200.0),
  (180, 'Winston Taylor', 3200.0),
  (194, 'Samuel McCain', 3200.0),
  (138, 'Stephen Stiles', 3200.0)   
]
# for i in range(5):  
#   # print(dict(zip(title,aa[i])))
#   b.append(dict(zip(title,aa[i])))
# print(b)
# print(type(b))
b=[]
for i in aa:
  b.append(dict(zip(title,i)))
print(b)

print(type(b))