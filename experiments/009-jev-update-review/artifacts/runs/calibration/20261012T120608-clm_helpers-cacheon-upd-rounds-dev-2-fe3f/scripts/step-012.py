import json,re
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-05/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:130]) for i,l in enumerate(L) if re.search('ERROR|FATAL|SERVFAIL|cert|pool|inflight',l,re.I)]
  print(s,len(h));[print(' ',x) for x in h[:3]]
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]
n['body']+='\nR5: board.md:3 Thread A mitigated (CHG-143 APPLIED changes.md:3 inventory-svc); board.md:4 Thread B +shipping-svc; follow-ups OPEN VENDOR_TICKET board.md:5, ALERT_TUNING board.md:6.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))