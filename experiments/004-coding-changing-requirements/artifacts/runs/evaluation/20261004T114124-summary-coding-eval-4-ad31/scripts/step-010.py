s=open('/task/workspace/invoice/core.py').read()
print('return amt' in s, 'q < 0:' in s, 'ROUND_HALF_EVEN' in s, 'tax_exempt' in s, 'return r2(amt)' in s)
from decimal import Decimal
import sys;sys.path.insert(0,'/task/workspace')
from invoice import compute_invoice
print(compute_invoice([{'sku':'a','qty':0,'unit_price':'1'},{'sku':'b','qty':3,'unit_price':'0.335'}],{'tier':'gold','region':'x','tax_exempt':True}))
try: compute_invoice([{'sku':'a','qty':-1,'unit_price':'1'}],{'tier':'x','region':'x'});print('no err')
except ValueError: print('ok neg')