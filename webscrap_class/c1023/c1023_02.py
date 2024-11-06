#파일 저장
import csv
st_list=['순위', '종목명', '검색비율', '현재가', '전일비', '등락률', '거래량', '시가', '고가', '저가', 'PER', 'ROE']
st_list1=['1', '삼성전자', '11.68%', '57,800', '상승100', '+0.17%', '7,827,861', '57,500', '58,200', '57,100', '14.13', '4.15']
st_list2=['2', 'SK하이닉스', '3.25%', '190,600', '상승2,800', '+1.49%', '747,655', '188,500', '191,800', '188,000', '55.54', '-15.61']
#csv파일로 저장 - 리스트로 바로 저장
with open("a.csv","w",encoding="utf-8",newline="") as f: 
  # newline="" : 줄바꿈 안함 # 한글이 깨질경우 : utf-8-sig
  writer = csv.writer(f)
  writer.writerow(st_list)
  writer.writerow(st_list1)
  writer.writerow(st_list2)
print("완료")