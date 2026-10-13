import json,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f).read().splitlines(),1):print(f,i,l)
for p in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if any(k in l for k in ['ERROR','FATAL','CRIT']) or ('WARN' in l and 'slow query' not in l):print(p.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
json.dump(c,open('/task/workspace/context.json','w'))