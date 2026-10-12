import json,re
d=json.load(open('/task/workspace/context.json'))
n=[x for x in d['entries'] if x['id']=='n1'][0]
n['body']+=' R8: board.md:3 Thread B cause revised DISK_PRESSURE (payments-svc, supersedes CACHE_STAMPEDE); board.md:4 Thread C pricing-svc failures cause unknown ongoing (check CHG-120 batch_size).'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))
for s in ['pricing-svc','ledger-svc','payments-svc']:
  L=open(f'/task/fixtures/round-08/logs/{s}.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|batch|config|disk|heap|429',l,re.I)]
  print(s,len(h),h[0][0] if h else '',h[-1][0] if h else '')
  for i,l in h[:3]: print(i,l[:200])