import json,re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['search-api','notify-worker','shipping-svc','inventory-svc','ledger-svc']:
  h=[i for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search('fail|error|disk|expired|SERVFAIL|max_inflight',l,re.I)]
  print(s,h[:12])
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open(p,'w'))