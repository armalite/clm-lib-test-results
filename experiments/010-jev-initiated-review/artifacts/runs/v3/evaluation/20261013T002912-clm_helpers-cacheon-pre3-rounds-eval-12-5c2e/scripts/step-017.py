import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3')]
e.append({'id':'n4','role':'note','body':'R4: board Thread B ledger-svc suspected QUEUE_BACKLOG ongoing (round-04/board.md:3). CHG-129 PROPOSED only (round-04/changes.md:3). Logs: inventory-svc certificate_expired peer=sso.example.net lines 3,15,26,35,55,56 (n=7); ledger-svc upstream returned 429? upstream=tax-provider retry_after_s lines 2,12,15,24,28,32 (n=12) -> likely UPSTREAM_RATE_LIMIT not queue; verify status code. pricing-svc output truncated: check pricing-svc errors in R4. Next: check R4 pricing-svc + ledger code, then advance.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
import re
for i,l in enumerate(open('/task/fixtures/round-04/logs/ledger-svc.log'),1):
  if i in(2,12):print(i,l.strip()[:160])
for i,l in enumerate(open('/task/fixtures/round-04/logs/pricing-svc.log'),1):
  if re.search('ERROR|WARN|fail|miss|evict',l,re.I) and 'slow query' not in l:print('p',i,l.strip()[:140])