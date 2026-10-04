import subprocess,sys,re
p='/task/workspace/invoice/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines()):
    if 'gold' in l or 'silver' in l: print(i,l)
