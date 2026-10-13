import re,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines(),1):
    if 'archiv' in l or 'status' in l: print(i,l)
