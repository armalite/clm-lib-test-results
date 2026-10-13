import json
r='/task/fixtures/round-09/logs/'
for s,L in [('search-api.log',None),('auth-svc.log',[22,55]),('shipping-svc.log',[28,34,56]),('inventory-svc.log',[59])]:
  ls=open(r+s).readlines()
  if L is None:
    a=[i for i,l in enumerate(ls,1) if '429' in l];b=[i for i,l in enumerate(ls,1) if 'max_inflight' in l]
    print(s,'429',a[:10],'cfg',b[:10]);print(ls[0][:200])
  else:
    for i in L:print(s,i,ls[i-1][:160].rstrip())
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n9','role':'note','body':'R9: board Thread C note pods restarting (round-09/board.md:3). CHG-166 APPLIED retry budget (noise). see next obs for line classes.'})
json.dump(c,open('/task/workspace/context.json','w'))