import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']=c['entries'][0]['body'].replace(' Next: advance to R4.','')+' R4: board.md:3 Thread A mitigated; board.md:4 OPEN RUNBOOK_UPDATE; changes.md:4 CHG-136 APPLIED mitigation A on ledger-svc; CHG-128 retry budget=1.'
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  L=open(f).read().splitlines();h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|429|disk|cache|pool|cert|dns|memory|lag|batch',l,re.I)]
  print(f.split('/')[-1],len(h),h[:15]);
  if h:print(' ',L[h[0]-1][:150])