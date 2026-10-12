import json
print(open('/task/fixtures/round-11/board.md').read())
for s in ['ledger-svc','checkout-api','payments-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-11/logs/{s}.log'),1):
    if 'ERROR' in l or 'used_pct' in l or 'pool' in l: print(s,i,l.strip()[:150])
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' R11: changes.md:3 CHG-181 irrelevant.'
json.dump(d,open('/task/workspace/context.json','w'))