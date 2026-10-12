import re,json
for s in ['auth-svc','checkout-api','ledger-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-10/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:150]) for i,l in enumerate(L) if re.search('WARN|ERROR|error|fail|exhaust|certif|disk|invalid',l,re.I) and 'slow' not in l]
  print(s,len(h));[print(x) for x in h[:4]]
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+='\nR9 logs: auth-svc cert_expired continues (round-09/logs/auth-svc.log:6,22); others clean.\nR10: board.md:3 Thread C checkout-api pod request failures, cause unknown, ongoing. changes.md:3 CHG-173 PROPOSED ignore.'
json.dump(c,open('/task/workspace/context.json','w'))