import json,re
r='/task/fixtures/round-09/'
print(open(r+'board.md').read());print(open(r+'changes.md').read())
for s in ['notify-worker','payments-svc','checkout-api','auth-svc','search-api']:
  L=[(i,l.strip()[:110]) for i,l in enumerate(open(r+'logs/'+s+'.log'),1) if re.search('ERROR|WARN|429|config|exhaust',l)]
  print(s,len(L),[i for i,_ in L][:10]);print(L[:1])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))