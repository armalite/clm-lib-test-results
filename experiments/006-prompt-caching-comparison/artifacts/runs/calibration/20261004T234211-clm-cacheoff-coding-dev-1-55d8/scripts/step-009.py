p='/task/workspace/invoice/core.py'
s=open(p).read()
import re
for i,l in enumerate(s.splitlines(),1):
    if 'gold' in l or 'silver' in l or 'format_money' in l or 'NotImplemented' in l: print(i,l)
print(open('/task/workspace/invoice/__init__.py').read())