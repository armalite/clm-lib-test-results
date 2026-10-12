import json,re
b='/task/fixtures/round-04/logs/'
for s in ['checkout-api','inventory-svc','ledger-svc','payments-svc','pricing-svc']:
  L=open(b+s+'.log').read().splitlines()
  hits=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|WARN|429|disk|used_pct|miss|batch',l,re.I) and 'slow' not in l.lower()]
  print(s,len(hits));[print(' ',h) for h in hits[:5]]
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR4: Thread A mitigated (round-04/board.md:3); CHG-136 APPLIED mitigation ledger-svc (round-04/changes.md:4); CHG-128 retry GETs=1 (changes.md:3). Follow-up OPEN RUNBOOK_UPDATE (board.md:4).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))