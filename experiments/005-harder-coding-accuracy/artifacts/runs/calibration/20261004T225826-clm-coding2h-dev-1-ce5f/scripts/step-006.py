p='/task/workspace/invoice/core.py'
s=open(p).read()
import re
for i,l in enumerate(s.splitlines()):
    if 'ship' in l or 'discount' in l or 'total' in l: print(i,l)