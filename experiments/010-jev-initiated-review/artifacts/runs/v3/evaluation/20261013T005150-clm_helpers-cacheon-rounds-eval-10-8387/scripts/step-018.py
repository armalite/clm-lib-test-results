import re,json
b='/task/fixtures/round-06/'
out=[]
for s in ['auth-svc','checkout-api','search-api','inventory-svc','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[i+1 for i,l in enumerate(L) if re.search('ERROR|error',l) and 'slow query' not in l]
  m=set(re.sub(r'.*"msg":"([^"]*)".*?("upstream":"[^"]*"|"host":"[^"]*")?.*',r'\1 \2',L[i-1])[:80] for i in e)
  out.append(f'{s} n={len(e)} {e[:1]}-{e[-1:]} {m}')
print('\n'.join(out))
n=open('notes.md').read()+'R6: board A mitigated (round-06/board.md:3), CHG-150 APPLIED auth-svc mitigation (round-06/changes.md:3); B cause UPSTREAM_RATE_LIMIT (board.md:4); OPEN ALERT_TUNING (:5). '+'; '.join(out)+'\n'
open('notes.md','w').write(n)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('context.json','w'))