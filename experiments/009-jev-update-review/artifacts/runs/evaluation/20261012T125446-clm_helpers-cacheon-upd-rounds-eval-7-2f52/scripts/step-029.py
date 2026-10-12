import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*.log')):
  L=open(f).read().splitlines()
  h=[i+1 for i,l in enumerate(L) if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l]
  print(f.split('/')[-1],len(h),h[:6],L[h[0]-1][:160] if h else '')
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n10','role':'note','body':'R10: board.md:3 Thread B DISK_PRESSURE mitigated. :4 Thread C ledger-svc still ongoing. :5 CLOSED RUNBOOK_UPDATE.'})
json.dump(c,open('/task/workspace/context.json','w'))