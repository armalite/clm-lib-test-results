import re,json
b='/task/fixtures/round-08/'
for fn in ['board.md','changes.md']:
  for i,l in enumerate(open(b+fn),1):print(fn,i,l.rstrip()[:200])
import os
for s in os.listdir(b+'logs'):
  h=[i for i,l in enumerate(open(b+'logs/'+s),1) if re.search('ERROR|heap|429|dns|restart|oom',l,re.I)]
  print(s,len(h),h[:12])
  for i,l in enumerate(open(b+'logs/'+s),1):
    if h and i==h[0]:print(l.strip()[:180])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))