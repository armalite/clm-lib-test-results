import json,re
for s in ['checkout-api','auth-svc','ledger-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-05/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:140]) for i,l in enumerate(L) if re.search(r'ERROR|pool|certif|memory|429|disk',l,re.I)]
  print(s,len(h));[print(x) for x in h[:4]]
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n+='\nR4 logs: auth cert_expired continues (round-04/logs/auth-svc.log:3,5,7). No checkout errors R4.\nR5: OPEN CAPACITY_REVIEW (round-05/board.md:3).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))