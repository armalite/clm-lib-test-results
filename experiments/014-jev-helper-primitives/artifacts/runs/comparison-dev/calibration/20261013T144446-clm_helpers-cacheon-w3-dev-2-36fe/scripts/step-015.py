import json,subprocess,sys,re
p='/task/workspace/exporter/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines()):
    if 'eu' in l or 'region' in l: print(i+1,l)
