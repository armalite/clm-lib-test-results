import json,re
for s in ['auth-svc','checkout-api','ledger-svc']:
  for i,l in enumerate(open(f'/task/fixtures/round-03/logs/{s}.log'),1):
    if re.search(r'ERROR|WARN|mem|rss|restart|pool',l,re.I) and 'slow' not in l: print(s,i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: board.md:3 Thread B auth-svc MEMORY_LEAK ongoing (verify vs logs).'})
json.dump(c,open('/task/workspace/context.json','w'))