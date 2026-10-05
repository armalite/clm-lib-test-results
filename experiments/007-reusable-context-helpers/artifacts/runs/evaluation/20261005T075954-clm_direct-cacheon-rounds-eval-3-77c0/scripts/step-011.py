import re,json
b='/task/fixtures/round-04/logs/'
for n in ['checkout-api','search-api','payments-svc']:
  L=open(b+n+'.log').read().splitlines()
  h=[(i,l) for i,l in enumerate(L,1) if re.search(r'429|rate|disk|space|ENOSPC|full|warn|err',l,re.I) and 'slow query' not in l]
  print(n,len(h),[i for i,_ in h][:30])
  for i,l in h[:3]: print(' ',i,l[:180])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=" | R4: board.md:3 A mitigated; :4 Thread B checkout-api UPSTREAM_RATE_LIMIT ongoing; :5 Thread D search-api DISK_PRESSURE ongoing; :6-8 OPEN CUSTOMER_COMMS,POSTMORTEM_DRAFT,CAPACITY_REVIEW. changes.md:4 CHG-136 APPLIED mitigation A ledger. No ERROR lines in R4 logs (verify B/D)."
json.dump(c,open('/task/workspace/context.json','w'))