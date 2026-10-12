import json
p='/task/fixtures/round-03/logs/auth-svc.log'
for i,l in enumerate(open(p),1):
  s=l.lower()
  if 'error' in s or 'mem' in s or 'restart' in s or 'oom' in s: print(i,l.strip()[:140])
for f in ['checkout-api','search-api','shipping-svc','ledger-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-03/logs/{f}.log'),1):
    if 'ERROR' in l or 'disk' in l.lower(): print(f,i,l.strip()[:120])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR3: board.md:3 Thread B MEMORY_LEAK auth-svc ongoing (suspected; verify vs CHG-114).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))