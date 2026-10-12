import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R9: board.md:3 Thread A resolved; :4 Thread B cause revised DISK_PRESSURE; :5 Thread C ledger-svc failures ongoing cause unknown; :6 OPEN VENDOR_TICKET; changes CHG-163 irrelevant.'
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['ledger-svc','checkout-api','payments-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
  h=[(i+1,l) for i,l in enumerate(L) if re.search('WARN|ERROR|warn|error',l) and 'slow query' not in l]
  print(s,len(h))
  for i,l in h[:4]: print(i,l[:200])