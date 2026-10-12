import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4','n5')]
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for n in ['auth-svc','checkout-api','notify-worker','payments-svc','search-api']:
  L=open(b+'logs/'+n+'.log').readlines()
  h=[(i,l.strip()[:110]) for i,l in enumerate(L,1) if re.search(r'ERROR|error|pool|429|inflight|WARN',l)]
  print(n,len(h));[print(' ',i,l) for i,l in h[:4]]