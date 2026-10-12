import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+="\nR10: CHG-170 dashboards only (round-10/changes.md:3)."
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-10/board.md').read())
import re
for s in ['pricing-svc','payments-svc','checkout-api','ledger-svc','inventory-svc']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('ERROR|WARN|429|valid|disk|used_pct',l) and 'slow' not in l.lower()]
  print(s,h[:10], L[h[0]-1][:150] if h else '')