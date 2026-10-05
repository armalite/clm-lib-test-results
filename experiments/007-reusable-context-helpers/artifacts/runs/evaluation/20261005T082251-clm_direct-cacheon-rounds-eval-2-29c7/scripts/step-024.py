import json,re
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'].startswith('n')]
json.dump(d,open(p,'w'))
b='/task/fixtures/round-08/'
for f in ('board.md','changes.md'):
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:250])
import os
skip=re.compile(r'request ok|heartbeat|gc |health ok|slow query|heap',re.I)
for s in sorted(os.listdir(b+'logs')):
  hits={}
  for i,l in enumerate(open(b+'logs/'+s),1):
    if skip.search(l) or not re.search(r'WARN|ERROR',l):continue
    m=re.search(r'"msg":"([^"]*)"',l);k=m.group(1) if m else l[:80]
    hits.setdefault(k,[]).append(i)
  for k,v in hits.items():print(s,k,v[:12],len(v))