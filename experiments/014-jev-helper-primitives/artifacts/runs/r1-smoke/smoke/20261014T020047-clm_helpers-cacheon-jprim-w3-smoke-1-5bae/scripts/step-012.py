import json,subprocess,sys
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s8.','s9.','s10.'))]
json.dump(c,open('/task/workspace/context.json','w'))
sys.path.insert(0,'/task/workspace')
import regtool; regtool.update(5)
p='/task/workspace/exporter/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines(),1): print(i,l)
