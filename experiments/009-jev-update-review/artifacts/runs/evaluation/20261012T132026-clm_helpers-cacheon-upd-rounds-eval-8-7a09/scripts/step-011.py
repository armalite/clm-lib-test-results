import json,glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if 'ERROR' in l or 'restart' in l.lower() or 'cert' in l.lower() or 'OOM' in l or 'pool' in l.lower()]
  print(f.split('/')[-1],len(hits))
  for h in hits[:3]: print(' ',h[0],h[1][:140])
print(open('/task/fixtures/round-05/board.md').read())
c=json.load(open('/task/workspace/context.json'))
b=[e for e in c['entries'] if e['id']=='n1'][0]['body']
b+='\nR5: changes.md:3 CHG-135 APPLIED health log sampling 1% (noise only).'
c['entries']=[{'id':'n1','role':'note','body':b}]
json.dump(c,open('/task/workspace/context.json','w'))