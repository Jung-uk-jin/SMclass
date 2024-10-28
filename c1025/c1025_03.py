
a = ['1만' ,'3,450','1.7만','500','1,000']

def chg(val):
  if '만' in val :
    r_val = float(val[:-1]*10000)
  else:
    r_val = float(val.replace(",",""))
  return r_val
a_list = list(map(chg,a))
print(a_list)
print(max(a_list))