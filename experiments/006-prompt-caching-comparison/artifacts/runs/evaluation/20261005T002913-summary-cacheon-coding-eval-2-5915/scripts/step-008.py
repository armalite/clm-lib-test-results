p='/task/workspace/invoice/core.py'
s=open(p).read()
import re
for i,l in enumerate(s.splitlines(),1):
    if 'tax' in l or 'PFX' in l or 'format' in l or 'abs' in l or 'return' in l: print(i,l)