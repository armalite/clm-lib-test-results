import json,re
for s in ['checkout-api','ledger-svc']:
  L=open(f'/task/fixtures/round-04/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'ERROR|WARN|pool|cache|miss|timeout',l,re.I)]
  print(s,len(h))
  for x in h[:8]: print(x)
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body'].replace(' Next: advance to R4.','')
n+=' R4: board.md:3 Thread B CACHE_STAMPEDE checkout-api ongoing; CHG-128 log sampling (irrelevant).'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))