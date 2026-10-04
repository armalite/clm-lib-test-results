import re
s=open('/task/workspace/invoice/core.py').read()
for i,l in enumerate(s.splitlines(),1):
    if any(k in l for k in ['tax','def ','customer','format','PREFIX','return']): print(i,l)