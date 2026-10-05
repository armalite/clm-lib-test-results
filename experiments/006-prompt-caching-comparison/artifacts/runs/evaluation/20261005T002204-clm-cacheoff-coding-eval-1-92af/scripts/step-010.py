import re
p='/task/workspace/invoice/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines(),1):
    if re.search(r'def |tax|format',l):print(i,l)