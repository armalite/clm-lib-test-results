import sys;sys.path.insert(0,'/task/workspace')
from invoice import compute_invoice as c
for L in [[],[{'sku':'a','qty':-1,'unit_price':'1'}],[{'sku':'a','qty':1,'unit_price':'-1'}],[{'sku':'a','qty':True,'unit_price':'1'}],[{'sku':'a','qty':1,'unit_price':'x'}]]:
  try:c(L,{'tier':'x','region':'y'});print('NO ERR',L)
  except ValueError:print('ok')
print(c([{'sku':'a','qty':0,'unit_price':'5'},{'sku':'b','qty':1,'unit_price':'1.005'}],{'tier':'gold','region':'r','tax_exempt':True}))