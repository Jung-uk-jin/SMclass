class Circle:
  def __init__(self,length):
    self.length=length
  def get_length(self,length):
    self.length=length
  def set_lengtj(self,length):
    self.length=length
c1=Circle(10)
print(c1.length)
c1.set_lengtj(200)
print(c1.get_length)
c1.length=100
print(c1.length)
print(c1.get_length())