import json,os
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
c['entries'].append({'id':'n5','role':'note','body':'R5: board empty. ledger-svc DNS SERVFAIL rates.internal continues (round-05/logs/ledger-svc.log:14). Only slow-query WARNs elsewhere.'})
json.dump(c,open('/task/workspace/context.json','w'))
p='/task/fixtures/round-05/changes.md'
if os.path.exists(p):
  for i,l in enumerate(open(p),1):print(i,l.rstrip())
else:print('no changes')