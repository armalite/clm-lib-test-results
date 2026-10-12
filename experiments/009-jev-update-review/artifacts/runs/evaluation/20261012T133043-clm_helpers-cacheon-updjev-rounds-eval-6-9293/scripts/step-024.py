import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
b=c['entries'][0]['body'].replace(' Next: advance to R8.','')
b+=' R8: board.md:3 Thread B revised DISK_PRESSURE (confirms); board.md:4 Thread C pricing-svc failures cause unknown ongoing (suspect CHG-120 batch_size=0).'
c['entries'][0]['body']=b
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['pricing-svc','ledger-svc','payments-svc','inventory-svc','checkout-api']:
  L=open(f'/task/fixtures/round-08/logs/{s}.log').read().splitlines()
  hits=[(i+1,l[:150]) for i,l in enumerate(L) if re.search('ERROR|WARN',l) and 'slow' not in l.lower()]
  print(s,len(hits))
  for h in hits[:5]:print(h)