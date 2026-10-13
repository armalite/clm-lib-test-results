import subprocess,sys,json
p='/task/workspace/exporter/core.py'
s=open(p).read()
import re
for i,l in enumerate(s.split('\n')):
    if 'max_records' in l or 'exported_by' in l or 'res' in l: print(i,l)
