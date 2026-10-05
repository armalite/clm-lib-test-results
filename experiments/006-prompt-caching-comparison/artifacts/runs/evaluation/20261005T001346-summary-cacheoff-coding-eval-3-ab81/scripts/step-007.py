s=open('/task/workspace/invoice/core.py').read()
print('0.90' in s, ':,.2f' in s)
import sys;sys.path.insert(0,'/task/workspace')
from invoice import format_money,compute_invoice
print(format_money('-1234.5','NZD'),compute_invoice([{'sku':'a','qty':100,'unit_price':'1'}],{'tier':'x','region':'r'}))