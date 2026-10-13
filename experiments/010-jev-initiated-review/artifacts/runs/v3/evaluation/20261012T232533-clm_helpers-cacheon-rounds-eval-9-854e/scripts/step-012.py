import json,re
n=open('/task/workspace/context.json').read()
c=json.loads(n)
b=c['entries'][0]['body']+'\nR4: board round-04/board.md:3 Thread B DB_POOL_EXHAUSTED shipping-svc ongoing; :4 follow-up OPEN DATA_BACKFILL. changes.md:3 CHG-131 APPLIED TLS ticket hourly. DNS errs continue round-04/logs/inventory-svc.log:11-28, ledger-svc.log:5-27. disk WARNs 91-98% on notify-worker & shipping-svc (no errors yet; maybe noise). search-api 0 errs.'
c['entries']=[{'id':'n1','role':'note','body':b}]
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-04/logs/shipping-svc.log'),1):
  if re.search('pool|ERROR|timeout',l,re.I): print(i,l.rstrip()[:160])