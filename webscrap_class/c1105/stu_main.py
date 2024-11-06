import oracledb
import stu_func

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

while True:
  choice = stu_func.main_print()   ## 메인화면출력부분
  if choice == "1":
    stu_func.stu_insert()          ## 학생성적입력부분
  elif choice == "2":
    stu_func.stu_output()          ## 학생성적출력부분  
  elif choice == "3":
    stu_func.stu_select()
  elif choice == "4":
    stu_func.stu_sort()
  elif choice =="5":
    stu_func.stu_rank()
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break
