import json,re
for s in ['auth-svc','checkout-api','ledger-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('ERROR|WARN',l) and 'slow' not in l]
  print(s,len(h),h[:3],h[-1:] if h else '',L[h[0]-1][:150] if h else '')
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n11','role':'note','body':'R11: board.md:3 Thread B adds ledger-svc; :4 Thread B mitigated; :5 Thread C pods restarting ongoing; :6 CLOSED CUSTOMER_COMMS; changes.md:3 CHG-179 PROPOSED ignore.'})
json.dump(c,open('/task/workspace/context.json','w'))