import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  hits=[]
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l: hits.append((i,l.strip()[:110]))
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]: print(' ',h)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4','n5')]
c['entries'].append({'id':'n6a','role':'note','body':'R6: board.md:3 Thread A mitigated. changes.md:3 CHG-150 APPLIED mitigation thread A shipping-svc.'})
json.dump(c,open('/task/workspace/context.json','w'))