str1="안녕하세요.반갑습니다."
print(str1[1]) # 해당 인덱스 출력
print(str1[2:5]) #해당 범위출력 // 인덱스 2번재~5번쨰
print(str1[:5]) # 처음부터 숫자앞까지
print(str1[2:]) # 숫자부터 끝까지 
print(str1[1:10:2]) # [위치 : 숫자 앞까지 ; 2칸씩]
print(str1[1:10:3]) # [위치 : 숫자 앞까지 ; 3칸씩]
print(str1[::-1]) # 처음부터 끝까지 역순으로 

# 배열 : 범위가 정해지면 수정 불가
# 리스트 : 범위상관없음



# s1="안녕하세요"

# s2="안녕"
# print(s1+s2)

# input_str=input("글자 입력")

# if input_str=="":
#   print("글자 입력해야함")
# else:
#   print("입력 문자: ",input_str)
