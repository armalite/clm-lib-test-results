import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  hits=[(i,l.strip()) for i,l in enumerate(open(f),1) if re.search('ERROR|WARN|error|warn',l) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]: print(' ',h[0],h[1][:180])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: board.md:3 Thread B CACHE_STAMPEDE checkout-api ongoing. changes.md:3 CHG-128 APPLIED log sampling (irrelevant).'})
json.dump(c,open('/task/workspace/context.json','w'))