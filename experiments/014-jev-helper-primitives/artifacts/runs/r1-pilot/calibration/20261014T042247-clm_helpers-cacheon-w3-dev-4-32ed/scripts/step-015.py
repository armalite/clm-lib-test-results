p='/task/workspace/exporter/core.py'
s=open(p).read()
import re
for i,l in enumerate(s.split('\n')):
    if 'region' in l or 'eu' in l: print(i,l)
