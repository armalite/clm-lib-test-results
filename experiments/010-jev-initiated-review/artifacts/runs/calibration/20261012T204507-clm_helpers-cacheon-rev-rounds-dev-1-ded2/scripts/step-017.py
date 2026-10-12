import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
c['entries'].append({'id':'n5','role':'note','body':'R5: Thread A mitigated after CHG-143 APPLIED auth-svc mitigation (round-05/board.md:3; round-05/changes.md:4). Thread B now also checkout-api, cause CACHE_STAMPEDE per board (round-05/board.md:4) but logs still 429 fx-rates: checkout round-05/logs/checkout-api.log:21,23,30; payments round-05/logs/payments-svc.log:13. Follow-up OPEN CAPACITY_REVIEW (round-05/board.md:5). CHG-138 TLS irrelevant. Next: advance R6.'})
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-05/logs/'
for n in ['auth-svc','notify-worker','search-api']:
  print(n,[i for i,l in enumerate(open(b+n+'.log'),1) if re.search(r'ERROR|pool|inflight',l)][:15])