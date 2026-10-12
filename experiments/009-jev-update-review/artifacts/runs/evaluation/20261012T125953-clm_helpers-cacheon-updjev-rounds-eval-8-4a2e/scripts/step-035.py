import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R12: board.md:3 DATA_BACKFILL CLOSED.'
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['inventory-svc','payments-svc','notify-worker','auth-svc','pricing-svc']:
  L=open(f'/task/fixtures/round-12/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search('exhaust|config validation|heap|dns|restart',l,re.I)]
  print(s,h[:12])