import json,re
R='/task/fixtures/round-11/'
print(open(R+'board.md').read())
for s in ['checkout-api','inventory-svc','shipping-svc','pricing-svc','search-api']:
  L=open(R+'logs/'+s+'.log').readlines()
  h=[i+1 for i,l in enumerate(L) if re.search('ERROR|error|fail|429',l) and 'slow' not in l]
  print(s,h[:12],L[h[0]-1][:160] if h else '')
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))