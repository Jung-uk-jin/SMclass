class Circle:
  def __init__(self,length):
    self.length=length
  def area(self):
    return 3.14*self.length**2
  def circum(self):
    return 3.14*2*self.length
  def __str__(self):
    c_str="원의 길이 : {}, 원의 넓이 : {}, 원의 둘레 : {:.2f}".format(self.length, self.area, self.circum)
    return c_str
c1 = Circle(int(input("반지름 입력 : ")))
print("넓이 : ",c1.area())
print("둘레 : ",c1.circum())

c2 = Circle(int(input("반지름 입력 : ")))
print("넓이 : ",c2.area())
print("둘레 : ",c2.circum())