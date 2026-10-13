import re
for s in ['search-api','auth-svc','shipping-svc']:
  L=open(f'/task/fixtures/round-08/logs/{s}.log').readlines()
  h=[(i,l.strip()[:150]) for i,l in enumerate(L,1) if ('ERROR' in l or 'WARN' in l) and 'slow' not in l.lower()]
  print(s,len(h))
  seen=set()
  for i,l in h:
    k=re.sub(r'\d','',l[40:110])
    if k not in seen:seen.add(k);print(i,l)