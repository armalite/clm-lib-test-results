import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R5 logs: only payments disk WARN round-05/logs/payments-svc.log:1-73. R6: board.md:3 Thread D MEMORY_LEAK ledger-svc ongoing; changes.md:3 CHG-147 PROPOSED (ignore).'
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  L=open(f).read().splitlines();h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|429|disk|cache|pool|cert|dns|memory|rss|heap|oom|restart|lag|batch',l,re.I)]
  print(f.split('/')[-1],len(h),h[:15])
  if h:print(' ',L[h[0]-1][:150])