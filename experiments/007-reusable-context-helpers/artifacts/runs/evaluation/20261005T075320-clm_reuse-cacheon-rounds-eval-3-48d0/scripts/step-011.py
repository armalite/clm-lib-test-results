import ctx,json,re
for f in ['checkout-api','inventory-svc','ledger-svc','payments-svc']:
  for i,l in enumerate(open('/task/fixtures/round-04/logs/'+f+'.log'),1):
    if re.search(r'WARN|ERROR|429|status=5|fail',l) and 'slow query' not in l:print(f,i,l.rstrip()[:140])
ctx.keep_only(['n1','n2','n3'])
d=json.load(open('context.json'))
d['entries'].append({'id':'n4','role':'note','body':'R4: board.md:3 A mitigated; :4 Thread B checkout-api UPSTREAM_RATE_LIMIT ongoing (suspected); :5 Thread D DISK_PRESSURE search-api ongoing; :6-8 OPEN CUSTOMER_COMMS,POSTMORTEM_DRAFT,CAPACITY_REVIEW. changes.md:4 CHG-136 APPLIED ledger mitigation A; :3 CHG-133 retry. search-api.log:12,13,21,38,54,62 disk WARN 92-98%.'})
json.dump(d,open('context.json','w'))