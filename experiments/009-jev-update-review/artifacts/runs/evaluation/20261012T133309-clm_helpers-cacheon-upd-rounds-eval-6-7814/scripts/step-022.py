import json,re
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R8: board.md:3 Thread B revised DISK_PRESSURE; board.md:4 Thread C pricing-svc failures ongoing cause unknown (suspect CHG-120 batch_size=0).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['pricing-svc','ledger-svc','payments-svc','checkout-api','inventory-svc']:
  L=open(f'/task/fixtures/round-08/logs/{s}.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|error|warn',l) and 'slow query' not in l]
  print(s,len(h),h[0][0] if h else '',h[-1][0] if h else '')
  for i,l in h[:2]: print(' ',i,l[:200])