import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n12','role':'note','body':'R12: changes.md:3 CHG-185 APPLIED dashboards noise. Next: read board, logs, then final.'})
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-12/'
print(open(b+'board.md').read())
for s in ['auth-svc','checkout-api','ledger-svc','search-api','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  h=[str(i+1) for i,l in enumerate(L) if re.search('ERROR|WARN|expired|pool|disk',l)]
  print(s,len(h),','.join(h[:20]))
  if h: print(L[int(h[0])-1][:200])