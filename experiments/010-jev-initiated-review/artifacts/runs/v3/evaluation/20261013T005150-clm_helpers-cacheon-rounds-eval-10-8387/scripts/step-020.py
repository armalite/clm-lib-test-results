import re,json
b='/task/fixtures/round-07/'
print(open(b+'board.md').read())
out=[]
for s in ['auth-svc','checkout-api','search-api','inventory-svc','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[i+1 for i,l in enumerate(L) if re.search('ERROR|error|WARN',l) and 'slow query' not in l]
  m=set(re.sub(r'.*"msg":"([^"]*)".*?("upstream":"[^"]*"|"host":"[^"]*")?.*',r'\1 \2',L[i-1])[:80] for i in e)
  out.append(f'{s} n={len(e)} {e[:1]}-{e[-1:]} {m}')
print('\n'.join(out))
print(open(b+'logs/inventory-svc.log').read().splitlines()[0][:300])
n=open('notes.md').read()+'R7: '+'; '.join(out)+'\n'
open('notes.md','w').write(n)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('context.json','w'))