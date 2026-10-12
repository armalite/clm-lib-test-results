import json,re
for s in ['checkout-api','auth-svc','ledger-svc']:
  L=open(f'/task/fixtures/round-04/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:150]) for i,l in enumerate(L) if re.search(r'ERROR|pool|certif|memory|429',l,re.I)]
  print(s,len(h));[print(x) for x in h[:5]]
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n+='\nR4: Thread A mitigated (round-04/board.md:3) via CHG-136 APPLIED search-api (round-04/changes.md:4). OPEN DATA_BACKFILL (board:4), VENDOR_TICKET (board:5). CHG-131 PROPOSED ignore.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))