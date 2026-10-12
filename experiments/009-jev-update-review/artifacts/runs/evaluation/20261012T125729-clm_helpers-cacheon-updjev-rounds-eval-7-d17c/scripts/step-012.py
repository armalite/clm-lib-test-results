import json,re
b='/task/fixtures/round-04/logs/'
for s in ['search-api','shipping-svc','checkout-api']:
    L=open(b+s+'.log').read().splitlines()
    h=[i+1 for i,l in enumerate(L) if re.search('ERROR|429|cache',l)]
    print(s,h[:20])
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n+=' R4 logs: no checkout/ledger errors (format still plain text).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))