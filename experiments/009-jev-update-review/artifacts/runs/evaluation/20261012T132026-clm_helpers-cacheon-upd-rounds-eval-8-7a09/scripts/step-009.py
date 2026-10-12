import json,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[(i+1,l) for i,l in enumerate(L) if 'ERROR' in l or 'restart' in l.lower() or 'cert' in l.lower() or 'OOM' in l]
  print(f.split('/')[-1],len(hits))
  for h in hits[:3]: print(' ',h[0],h[1][:140])
c=json.load(open('/task/workspace/context.json'))
b=[e for e in c['entries'] if e['id']=='n1'][0]['body']
b+='\nR4: board.md:3 Follow-up OPEN ALERT_TUNING.'
c['entries']=[{'id':'n1','role':'note','body':b}]
json.dump(c,open('/task/workspace/context.json','w'))