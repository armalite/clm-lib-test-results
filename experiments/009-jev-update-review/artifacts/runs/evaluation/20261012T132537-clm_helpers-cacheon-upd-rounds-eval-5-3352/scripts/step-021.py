import json,re
for s in ['auth-svc','checkout-api','search-api','shipping-svc','ledger-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-09/logs/{s}.log'),1):
    if re.search(r'ERROR|certificate|pool|disk|exhaust|429|dns|lag|memory',l,re.I) and 'slow' not in l.lower(): print(s,i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))