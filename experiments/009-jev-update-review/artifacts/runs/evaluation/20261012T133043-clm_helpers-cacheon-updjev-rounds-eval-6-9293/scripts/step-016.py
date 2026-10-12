import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R4 logs: only payments disk WARN (round-04/logs/payments-svc.log:4-73); ledger/inventory 429 gone. R5: board.md:3 OPEN VENDOR_TICKET.'
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  L=open(f).read().splitlines();h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|429|disk|cache|pool|cert|dns|memory|lag|batch',l,re.I)]
  print(f.split('/')[-1],len(h),h[:15])
  if h:print(' ',L[h[0]-1][:150])