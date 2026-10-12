import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  h=[(i,l) for i,l in enumerate(open(f),1) if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l]
  print(f.split('/')[-1],len(h),[i for i,_ in h][:8]);
  for i,l in h[:2]: print(' ',i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n8','role':'note','body':'R8: board.md:3 Thread B (CACHE_STAMPEDE per board) now also payments-svc, unchanged status ongoing. board.md:4 OPEN RUNBOOK_UPDATE. No changes.md. Logs: see below step.'})
json.dump(c,open('/task/workspace/context.json','w'))