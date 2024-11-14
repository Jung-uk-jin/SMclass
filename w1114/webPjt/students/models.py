from django.db import models

# Create your models here.
# 오라클에서 table 생성 가능 ,insert update select delete
class Student(models.Model):
  s_name = models.CharField(max_length=100)
  s_major = models.CharField(max_length=100)
  s_age = models.IntegerField(default=0)
  s_grade = models.IntegerField(default=0)
  s_gender = models.CharField(max_length=30)
def ___str___(self):
  return self.s_name