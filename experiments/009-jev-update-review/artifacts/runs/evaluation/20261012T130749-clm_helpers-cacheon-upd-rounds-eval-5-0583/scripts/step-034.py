import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='sum1']
c['entries'][0]['body']=c['entries'][0]['body'].replace('Next: advance to R12.','R12 released: CHG-185 APPLIED dashboards only (round-12/changes.md:3).')
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-12/board.md').read())
for f in ['checkout-api','ledger-svc','auth-svc']:
  n=0
  for i,l in enumerate(open(f'/task/fixtures/round-12/logs/{f}.log'),1):
    if re.search('pool_max|certificate',l):
      n+=1
      if n<=3:print(f,i,l.strip()[:120])
  print(f,'count',n)