import json,re
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']+='\nR11: board.md:3 Thread B +ledger-svc; :4 Thread B mitigated; :5 Thread C still restarting; :6 CLOSED CUSTOMER_COMMS; changes:3 CHG-179 PROPOSED ignore.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['auth-svc','checkout-api','ledger-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|cert|pool|disk|config',l,re.I)]
  print(s,len(h),h[:3])