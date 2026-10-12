import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
c['entries'][0]['body']+=' R5: CHG-137 PROPOSED HPA search (not applied, noise).'
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-05/board.md').read())
b='/task/fixtures/round-05/logs/'
for s in ['checkout-api','ledger-svc','payments-svc','search-api','shipping-svc']:
  n=0
  for i,l in enumerate(open(b+s+'.log'),1):
    if re.search(r'ERROR|disk|429|pool|cache',l,re.I) and n<3: print(s,i,l.strip()[:110]);n+=1
