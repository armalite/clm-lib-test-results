import re
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip())
c={}
for i,l in enumerate(open(b+'logs/returns-svc.log'),1):
 if 'ERROR' in l:
  k=re.sub(r'\d+','N',l[50:100])
  c.setdefault(k,[]).append(i)
for k,v in c.items():print(len(v),v[:3],k)
for i,l in enumerate(open(b+'logs/edge-gw.log'),1):
 if ' 503' in l or '503 ' in l:print(i,l.rstrip()[:140]);break