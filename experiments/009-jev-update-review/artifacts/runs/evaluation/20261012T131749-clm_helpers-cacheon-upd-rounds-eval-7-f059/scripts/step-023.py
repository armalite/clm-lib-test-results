import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  hits=[i for i,l in enumerate(open(f),1) if ('WARN' in l or 'ERROR' in l or 'error' in l.lower()) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits),hits[:5])
  for i in hits[:1]: print(open(f).read().splitlines()[i-1][:200])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R8: board.md:3 Thread B adds payments-svc (cause still CACHE_STAMPEDE on board); :4 OPEN RUNBOOK_UPDATE.'
json.dump(c,open('/task/workspace/context.json','w'))