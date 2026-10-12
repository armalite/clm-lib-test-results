import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
c['entries'][0]['body']+=' R6: Thread A mitigated (round-06/board.md:3); CHG-150 APPLIED mitigation shipping-svc (round-06/changes.md:3).'
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-06/logs/'
for s in ['checkout-api','ledger-svc','payments-svc','search-api','shipping-svc']:
  n=0
  for i,l in enumerate(open(b+s+'.log'),1):
    if re.search(r'ERROR|disk|upstream|pool',l,re.I) and n<3: print(s,i,l.strip()[:110]);n+=1
