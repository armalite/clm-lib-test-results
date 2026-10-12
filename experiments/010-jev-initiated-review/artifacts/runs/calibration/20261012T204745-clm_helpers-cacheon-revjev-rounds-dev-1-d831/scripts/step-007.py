import json,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f).read().splitlines(),1): print(f,i,l[:200])
for p in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  L=open(p).read().splitlines();s=p.split('/')[-1]
  hits=[(i,l) for i,l in enumerate(L,1) if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l]
  print(s,len(hits))
  for i,l in hits[:6]: print(' ',i,l[:130])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))