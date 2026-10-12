import json,re
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance to R6.','')
n+=' R6: board.md:3 Thread A mitigated; changes.md:3 CHG-150 APPLIED mitigation shipping-svc.'
import glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  L=open(f).read().splitlines()
  hits=[i+1 for i,l in enumerate(L) if re.search(r'429|disk|pool|miss|cert|dns|lag|oom|memory',l,re.I)]
  print(f.split('/')[-1],len(hits),hits[:15])
  for i in hits[:2]: print(' ',L[i-1][:160])
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))