import json,subprocess,sys,re
p='/task/workspace/exporter/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines(),1):
    if 'archived' in l or 'strip' in l: print(i,l)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s5.','s7.'))]
json.dump(c,open('/task/workspace/context.json','w'))
sys.path.insert(0,'/task/workspace')
import regtool; regtool.update(4)