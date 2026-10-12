import json,re
L=open('/task/fixtures/round-06/logs/checkout-api.log').read().splitlines()
h=[(i+1,l[:150]) for i,l in enumerate(L) if re.search(r'ERROR|pool',l,re.I)]
print(len(h));[print(x) for x in h[:5]]
for s in ['auth-svc','search-api','shipping-svc','ledger-svc']:
  L=open(f'/task/fixtures/round-06/logs/{s}.log').read().splitlines()
  h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|certif|disk',l,re.I)]
  print(s,len(h),h[:6])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n+='\nR6: Thread D DB_POOL_EXHAUSTED checkout-api ongoing (round-06/board.md:3); likely from CHG-113 (round-01/changes.md:4). CHG-147 benign.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))