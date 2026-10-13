import re,collections
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
for s in ['inventory-svc','ledger-svc','notify-worker','search-api','shipping-svc']:
  c=collections.Counter();first={}
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if 'slow' in l.lower():continue
    k=re.sub(r'\d+','N',l.strip())[20:90]
    if 'ERR' in l or 'WARN' in l or 'error' in l.lower():
      c[k]+=1;first.setdefault(k,[i,i]);first[k][1]=i
  for k,v in c.most_common(4):print(s,v,first[k],k)