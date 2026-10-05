import sys;sys.path.insert(0,'/task/workspace')
from invoice import compute_invoice as c
for L in [[],[{'sku':'a','qty':-1,'unit_price':'1'}],[{'sku':'a','qty':1,'unit_price':'-1'}],[{'sku':'a','qty':True,'unit_price':'1'}],[{'sku':'a','qty':1,'unit_price':'nan'}]]:
  try:print(c(L,{'tier':'gold','region':'x'}))
  except ValueError as e:print('VE',e)
print(c([{'sku':'a','qty':0,'unit_price':'5'},{'sku':'b','qty':1,'unit_price':'10'}],{'tier':'gold','region':'x','tax_exempt':True}))