import json,collections
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip(): print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  g=collections.OrderedDict()
  for i,l in enumerate(open(b+'logs/'+f),1):
    try:
      d=json.loads(l);lv=d.get('level');m=d.get('msg');ex={k:v for k,v in d.items() if k not in('ts','level','svc','msg','ms','table')}
    except Exception:
      p=l.split();lv=p[1] if len(p)>1 else '';m=' '.join(p[3:6]);ex=''
    if lv=='INFO' or 'slow query' in str(m): continue
    g.setdefault((lv,m,str(ex)),[]).append(i)
  for k,v in g.items(): print(f,k,[len(v),v[0],v[-1]])
