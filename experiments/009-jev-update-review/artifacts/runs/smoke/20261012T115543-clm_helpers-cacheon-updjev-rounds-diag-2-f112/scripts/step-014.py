import json,re
R='/task/fixtures/round-04/logs/'
for s in ['pricing-svc','search-api','inventory-svc','notify-worker','ledger-svc']:
  L=open(R+s+'.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'cert|SERVFAIL|disk|pool|429|ERROR|miss',l,re.I)]
  print(s,len(h));[print(' ',x) for x in h[:4]]
c=json.load(open('/task/workspace/context.json'))
b=c['entries'][0]['body'].replace(' Next: advance to R4.','')+' R4: board Thread A (CERT) mitigated round-04/board.md:3; CHG-136 APPLIED mitigation pricing-svc changes.md:4; CHG-128 PROPOSED ignore.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]},open('/task/workspace/context.json','w'))