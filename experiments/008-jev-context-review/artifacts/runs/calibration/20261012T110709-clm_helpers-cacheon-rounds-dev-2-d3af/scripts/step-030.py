import json,re
b='/task/fixtures/round-10/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[(i+1,l[:150]) for i,l in enumerate(L) if re.search('ERROR|error|429|fail|expired',l,re.I)]
  print(s,len(e),[x[0] for x in e]);
  for x in e[:2]:print(x)
p='/task/workspace/context.json'
n=json.load(open(p))['entries'][0]
json.dump({'format':'clm-context/v1','entries':[n]},open(p,'w'))