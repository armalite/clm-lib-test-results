import json,re
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']+="\nR9: Thread B +checkout-api, status mitigated (round-09/board.md:3,4). Thread C still restarting (board.md:5). Thread D ledger MEMORY_LEAK closed false alarm (board.md:6) -> drop. DATA_BACKFILL CLOSED (board.md:7)."
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['checkout-api','pricing-svc','payments-svc']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|WARN|disk|batch_size',l)]
  print(s,len(h));[print(x) for x in h[:5]]