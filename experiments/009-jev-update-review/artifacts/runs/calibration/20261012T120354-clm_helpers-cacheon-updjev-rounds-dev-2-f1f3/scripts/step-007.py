import json
L=open('/task/fixtures/round-03/logs/auth-svc.log').read().splitlines()
for i,l in enumerate(L,1):
  if any(k in l.lower() for k in ['pool','error','warn','timeout']): print(i,l[:140])
for s in ['search-api']:
  for i,l in enumerate(open(f'/task/fixtures/round-03/logs/{s}.log').read().splitlines(),1):
    if any(k in l.lower() for k in ['inflight','error','reject']): print(s,i,l[:140])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: board.md:3 Thread B auth-svc DB_POOL_EXHAUSTED ongoing (verify). changes.md:3 CHG-126 PROPOSED (ignore). R2 search-api logs showed no errors.'})
json.dump(c,open('/task/workspace/context.json','w'))