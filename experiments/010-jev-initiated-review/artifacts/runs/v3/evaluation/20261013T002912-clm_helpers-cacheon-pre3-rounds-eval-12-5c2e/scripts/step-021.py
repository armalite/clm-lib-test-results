import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4')]
e.append({'id':'n5','role':'note','body':'R5: board Follow-up OPEN CUSTOMER_COMMS (round-05/board.md:3). Logs: inventory-svc certificate_expired n=12 (round-05/logs/inventory-svc.log:10,16,19); search-api certificate_expired n=7 (round-05/logs/search-api.log:6,35,48); ledger-svc 429 tax-provider n=6 (round-05/logs/ledger-svc.log:7,35,39) confirmed UPSTREAM_RATE_LIMIT. pricing/checkout clean. Next: advance to R6.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')