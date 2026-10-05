import os,json,re
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
from collections import defaultdict
for f in sorted(os.listdir(b+'logs')):
  d=defaultdict(list)
  for i,l in enumerate(open(b+'logs/'+f),1):
    try:
      j=json.loads(l); lv=j.get('level'); m=j.get('msg'); ex={k:v for k,v in j.items() if k not in('ts','level','svc','msg')}
    except Exception:
      p=l.split(None,3); lv=p[1] if len(p)>1 else ''; m=l.strip()[25:90]; ex=''
    if lv in('INFO','DEBUG') or 'slow query' in str(m): continue
    d[(lv,str(m),str(ex)[:80])].append(i)
  for k,v in d.items(): print(f,k,v[0],v[-1],len(v))