import json,re
b='/task/fixtures/round-06/'
for s in ['checkout-api','ledger-svc','payments-svc','search-api','shipping-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    h=[(i+1,l[:90]) for i,l in enumerate(L) if re.search('ERROR|429|pool|cache|miss|cert|dns',l,re.I) and 'slow query' not in l]
    print(s,len(h),h[:3])
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n+=' R6: board:3 Thread A now MITIGATED; changes:3 CHG-150 APPLIED mitigation thread A shipping-svc.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))