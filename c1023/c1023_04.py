import time
import random

print(random.randint(1,3))

# a=[0]*100
# for i in range(100):
#   a[i]=i

b=[i for i in range(100)]

for i in b:
  print(i)
  time.sleep(random.uniform(1,3))

