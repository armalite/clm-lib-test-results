import json,re
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open(p,'w'))
b='/task/fixtures/round-12/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['inventory-svc','ledger-svc','pricing-svc','auth-svc','payments-svc']:
  for i,l in enumerate(open(b+'logs/'+s+'.log'),1):
    if re.search('ERROR|error|SERVFAIL|invalid|config',l): print(s,i,l.strip()[:110])
