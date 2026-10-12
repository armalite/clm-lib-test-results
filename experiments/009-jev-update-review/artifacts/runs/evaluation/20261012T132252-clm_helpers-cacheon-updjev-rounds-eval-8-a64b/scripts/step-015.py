import json,re
for s in ['notify-worker','inventory-svc','pricing-svc','auth-svc']:
  L=open(f'/task/fixtures/round-06/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'WARN|ERROR|error|fail|pool|dns|heap',l,re.I)]
  print(s,len(h));[print(x) for x in h[:5]]
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n3','n4','n5')]
c['entries'][-1]['body']=c['entries'][-1]['body'].replace(' Next: advance to R6.','')
c['entries'].append({'id':'n6','role':'note','body':'R6 board: A mitigated (round-06/board.md:3) via CHG-150 APPLIED pricing-svc (round-06/changes.md:4); D DNS_RESOLUTION notify-worker ongoing (round-06/board.md:4) - check vs CHG-113 pool config. CHG-147 irrelevant.'})
json.dump(c,open('/task/workspace/context.json','w'))