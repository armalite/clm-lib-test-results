import json,re
L=open('/task/fixtures/round-03/logs/inventory-svc.log').read().splitlines()
for i,l in enumerate(L):
    if re.search(r'cache|miss|WARN|warn|latency',l,re.I): print(i+1,l[:140])
c=json.load(open('/task/workspace/context.json'))
b=c['entries'][0]['body']+' R3 logs: pricing DNS+cert continue (pricing-svc.log:3,13), search-api cert (search-api.log:9).'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]},open('/task/workspace/context.json','w'))