import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|429|miss|exhaust|cert|dns|lag|oom|disk',l,re.I): print(f.split('/')[-1],i,l.strip()[:120])
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1']
e[0]['body']+='\nR4: board.md:3 Thread A mitigated; board.md:4 follow-up OPEN RUNBOOK_UPDATE; changes.md:3 CHG-128 APPLIED retry GETs=1; changes.md:4 CHG-136 APPLIED mitigation thread A ledger-svc.'
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))