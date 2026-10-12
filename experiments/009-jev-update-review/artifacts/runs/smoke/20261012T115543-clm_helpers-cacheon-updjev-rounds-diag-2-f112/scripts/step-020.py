import json,re
for s in ['inventory-svc','ledger-svc','notify-worker','pricing-svc','search-api']:
  L=open(f'/task/fixtures/round-06/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'ERROR|disk|cert|SERVFAIL|pool|429|miss|OOM|lag',l,re.I) and 'slow' not in l.lower()]
  print(s,len(h));[print(i,l) for i,l in h[:4]]
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0];n['body']+=' R6 board: ALERT_TUNING open round-06/board.md:3; POSTMORTEM_DRAFT open board.md:4.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))