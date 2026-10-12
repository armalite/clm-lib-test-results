import json,re
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-06/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:120]) for i,l in enumerate(L) if re.search('ERROR|FATAL|SERVFAIL|expired|exhaust|inflight|429',l,re.I)]
  print(s,len(h));[print(' ',x) for x in h[:2]]
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']+='\nR5 logs: cert errs auth-svc round-05/logs/auth-svc.log:2, shipping round-05/logs/shipping-svc.log:9; no DNS errs.\nR6: board.md:3 OPEN RUNBOOK_UPDATE; changes.md:3 CHG-144 log sampling (noise).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))