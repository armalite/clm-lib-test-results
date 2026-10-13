p='/task/workspace/exporter/core.py'
s=open(p).read()
import re
for l in s.split('\n'):
    if 'archived' in l or 'region' in l or 'strip' in l: print(l)
