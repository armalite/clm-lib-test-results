import json
ctx=json.load(open('/task/workspace/context.json'))
keep=[e for e in ctx['entries'] if e['id'].startswith('n')]
keep.append({'id':'n10a','role':'note','body':'Round 10 released (files round-10/board.md, changes.md, logs). Not yet analysed.'})
ctx['entries']=keep
json.dump(ctx,open('/task/workspace/context.json','w'))
import subprocess
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip())
import glob
for p in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
  for i,l in enumerate(open(p),1):
    if 'ERROR' in l or 'error' in l: print(p.split('/')[-1],i,l.strip()[:110])