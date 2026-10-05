import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: Thread A mitigated (round-04/board.md:3); CHG-136 APPLIED mitigation auth-svc (round-04/changes.md:4). Thread B ledger-svc suspected CACHE_STAMPEDE ongoing (board.md:4) BUT logs show DNS SERVFAIL host=rates.internal (round-04/logs/ledger-svc.log:10,28,47,51) -> likely DNS_RESOLUTION. Follow-up OPEN DATA_BACKFILL (board.md:5). CHG-133 APPLIED TLS ticket rotation hourly.'})
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-04/logs/ledger-svc.log'),1):
  if re.search(r'ERROR|cache|miss',l):print(i,l.rstrip()[:120])