class Car:
  def __init__(self,color,tire,gear,speed):
      self.color =color
      self.tire=tire
      self.gear=gear
      self.speed=speed



  def upSpeed(self,value):
    if value >0:
      self.speed+=value
    else:
      raise "값을 잘못 넣었음"
  def downSpeed(self,value):
    self.speed-=value

#클래스 사용하려면 [클래스 선언]
c1 = Car("흰색",4,"auto",0)
print(c1.color)