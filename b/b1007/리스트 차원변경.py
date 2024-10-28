a=[]
for i in range (25):
  a.append(i+1)
print(a)
b=[]
for i in range(0,len(a),5):
  b.append(a[i:i+5])
print(b)
# b=[]
# for j in range(5):
#   a=[]
#   for k in range(5):
#     a.append(5*i+(j+1))
#   b.append(a)
# print(b)
