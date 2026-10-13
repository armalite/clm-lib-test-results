import re,json
b='/task/fixtures/round-05/logs/'
out=[]
for s,p in [('auth-svc','dns lookup'),('checkout-api','dns lookup'),('search-api','429')]:
  L=open(b+s+'.log').read().splitlines()
  ix=[i+1 for i,l in enumerate(L) if p in l]
  out.append(f'{s}.log:{ix[0]}-{ix[-1]} n={len(ix)}' if ix else s+' none')
for s in ['inventory-svc','shipping-svc']:
  L=open(b+s+'.log').read().splitlines()
  e=[(i+1,l[:120]) for i,l in enumerate(L) if 'ERROR' in l]
  out.append(s+' ERR '+str(e[:3]))
r='R5: board empty; CHG-140 log sampling irrelevant. '+'; '.join(out)+'\n'
print(r)
n=open('notes.md').read()+r
open('notes.md','w').write(n)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('context.json','w'))