import json
for s in ['search-api','auth-svc']:
  L=open(f'/task/fixtures/round-02/logs/{s}.log').read().splitlines()
  print(s,len(L),L[0][:150])
  for i,l in enumerate(L,1):
    if any(k in l.lower() for k in ['inflight','error','fail','reject']): print(i,l[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
c['entries'][1]['body']+=' R2 checkout-api SERVFAIL rates.internal logs/checkout-api.log:8,24,29,38,46,59.'
json.dump(c,open('/task/workspace/context.json','w'))