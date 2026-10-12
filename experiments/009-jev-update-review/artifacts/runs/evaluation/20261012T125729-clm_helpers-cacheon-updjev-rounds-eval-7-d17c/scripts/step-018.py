import json,re
b='/task/fixtures/round-07/'
for s in ['checkout-api','ledger-svc','payments-svc','search-api','shipping-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    h=[(i+1,l[:90]) for i,l in enumerate(L) if re.search('ERROR|429|pool|cache|miss|cert|dns|disk|oom|lag',l,re.I) and 'slow query' not in l and 'heartbeat' not in l]
    print(s,len(h),h[:3])
print(open(b+'board.md').read())
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n+=' R7: changes:3 CHG-154 PROPOSED HPA (ignore).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))