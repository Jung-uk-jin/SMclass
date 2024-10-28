#class 생성 방법

#학생 1명 정보
#번호 이름 국어 영어 수학 합계 평균 등수
class student:
  # def __init__(self): # 기본생성자
  #   None
  def __init__(self,no,name,kor,eng,math): # 기본생성자
    self.no=no
    self.name=name
    self.kor=kor
    self.eng=eng
    self.math=math
    self.total=kor+eng+math
    self.avg=(kor+eng+math)/3
    self.rank=0
  def print(self):
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".
          format(self.no,self.name,self.kor,self.eng,self.math,self.total,self.avg,self.rank))

  def stu_input():
    pass
  def stu_output():
    pass

#전체 학생 정보
class students:
  #클래스 선언
  s1 = student(1,"홍",100,100,100)
  # print(s1) # 주소값 출력
  s1.print()
  #클래스 출력
