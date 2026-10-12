import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']=c['entries'][0]['body'].replace('\nNEXT: advance R12.','\nR12: changes.md:3 CHG-185 dashboards irrelevant; board.md 2 lines (header).')
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-12/board.md').read())
for s in ['auth-svc','checkout-api','ledger-svc','search-api','shipping-svc']:
  L=open(f'/task/fixtures/round-12/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|WARN|exhaust|disk|cert|config',l) and 'slow' not in l]
  print(s,len(h),h[:3])