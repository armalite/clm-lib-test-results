import re,subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines(),1):
    if 'ship' in l or 'total' in l: print(i,l)
