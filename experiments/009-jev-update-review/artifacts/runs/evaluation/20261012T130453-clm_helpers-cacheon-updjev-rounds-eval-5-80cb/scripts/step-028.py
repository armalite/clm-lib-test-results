import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
for x in c['entries']:
  if x['id']=='n9': x['body']='R9: board empty; no changes; auth-svc cert_expired continues (round-09/logs/auth-svc.log:6-71); others clean.'
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['checkout-api','auth-svc','ledger-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|error|fail',l) and 'slow' not in l]
  print(s,len(h),[i for i,_ in h][:40])
  for i,l in h[:3]: print(i,l[:200])