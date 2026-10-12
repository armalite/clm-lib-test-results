import json,re
b='/task/fixtures/round-04/logs/'
for s in ['checkout-api','ledger-svc']:
    L=open(b+s+'.log').read().splitlines()
    h=[i+1 for i,l in enumerate(L) if re.search('ERROR|pool|cache|miss',l,re.I)]
    print(s,h[:30])
    for i in h[:3]: print(i,L[i-1][:200])
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n+=' R4: board:3 Thread B CACHE_STAMPEDE checkout-api ongoing; changes:3 CHG-128 log sampling (noise).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))