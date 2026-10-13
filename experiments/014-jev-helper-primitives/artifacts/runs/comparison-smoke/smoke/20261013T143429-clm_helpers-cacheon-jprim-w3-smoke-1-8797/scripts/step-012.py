import sys,subprocess;sys.path.insert(0,'/task/workspace')
import reghelper as H
p='/task/workspace/exporter/core.py';s=open(p).read()
import re
for i,l in enumerate(s.splitlines()):
  if 'audit' in l or 'exported_by' in l: print(i,l)
c=H.load()
reg=[e for e in c['entries'] if e['id']=='register'][0]['body'].split('\n')
try:
  a=H.affected(reg,['S5.1 confidential also exportable when admin and purpose==regulator','S5.2 exported_by omitted for admin exports']);print(a)
except Exception as e: print('jev err',e)