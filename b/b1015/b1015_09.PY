# ab=[]

# def car(a,b):
#   for i in range(4):
#   ab.append(a[i]+b[i])

# a=[1,2,3,4]
# b=[10,20,30,40]



# print(ab)


a=[1,2,3,4,5]

#리스트 내포
r=[x+10 for x in a]
print(r)
#map과 람다
r2 = list(map(lambda x: x+10, a))
print(r2)

# zip ; 2개의 리스트를 1개로 변경
# a=[1,2,3,4]
# b=[8,9,7]
# print(list(zip(a,b)))
# print(dict(zip(a,b)))


# arr배열중에 2의 배수인 경우만 리턴
# arr = [1,2,3,4,5,6,7]
# brr = list(filter(lambda x:x%2==0,arr)) #조건에 만족한 부분만 데이터를 넘김
# print(brr)

# print(fun(2))

# arr = [1,2,3,4,5,6,7]
# barr =[]

# for i in arr:
#   barr.append(fun(i))
# print(barr)
# barr = map(fun,arr)

# 맵(함수, 리스트) : 리스트의 내용을 1개씩 함수에 
# 전달해서 결과값을 리스트로 저장

# print(type(barr))
# print(list(barr))

# barr = list(map(lambda x:x*2,arr))