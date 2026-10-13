import json,re
print(open('/task/fixtures/round-10/board.md').read())
print(open('/task/fixtures/round-10/changes.md').read())
for s in ['pricing-svc','checkout-api','ledger-svc','search-api','inventory-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-10/logs/{s}.log'),1):
    if re.search('ttl|429|cert|ERROR|error',l):print(s,i,l.strip()[:100])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))