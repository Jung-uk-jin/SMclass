member = [
  {"id":"aaa","pw":"1111","name":"홍길동","nicName":"길동스","address":"서울시","money":1000000000},
  {"id":"bbb","pw":"2222","name":"유관순","nicName":"관순스","address":"부산시","money":1000000000},
  {"id":"ccc","pw":"3333","name":"이순신","nicName":"순신스","address":"경기도","money":1000000000},
  {"id":"ddd","pw":"4444","name":"강감찬","nicName":"감찬스","address":"인천시","money":1000000000},
  {"id":"admin","pw":"5555","name":"김구","nicName":"김스","address":"대구시","money":1000000000},
]
f=open("member.txt","w",encoding='utf-8')
for m in member:
  f.write(f"{m['id']}, {m['pw']}, {m['name']}, {m['nicName']},{m['address']},{m['money']}\n ")
f.close()