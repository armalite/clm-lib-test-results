p='/task/workspace/exporter/core.py'
s=open(p).read()
import re
for i,l in enumerate(s.splitlines(),1):
    if 'archived' in l or 'status' in l: print(i,l)