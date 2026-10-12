import json
b='/task/fixtures/round-09/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','inventory-svc','search-api','shipping-svc']:
  L=open(b+'logs/%s.log'%s).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if 'ERROR' in l]
  ks={}
  for i,l in e:
    k=('config' if 'config validation' in l else '429' if '429' in l else 'cert' if 'cert' in l.lower() else 'dns' if 'dns' in l.lower() or 'resol' in l.lower() else l[:80])
    ks.setdefault(k,[]).append(i)
  print(s,{k:(len(v),v[0],v[-1]) for k,v in ks.items()})
p='/task/workspace/context.json'
n=json.load(open(p))['entries'][0]
json.dump({'format':'clm-context/v1','entries':[n]},open(p,'w'))