import json
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
  if e['id']=='n1': e['body']+='\nR9 board empty, no changes. R10: board.md:3 Thread C checkout-api pod failures cause unknown ongoing; changes:3 CHG-173 PROPOSED ignore.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
import re
for s in ['checkout-api','auth-svc','ledger-svc','search-api','shipping-svc']:
  n=0
  for i,l in enumerate(open(f'/task/fixtures/round-10/logs/{s}.log'),1):
    if re.search(r'ERROR|WARN|FATAL|error|fail',l) and 'slow' not in l.lower():
      n+=1
      if n<=4: print(s,i,l.rstrip()[:200])
  print(s,'count',n)