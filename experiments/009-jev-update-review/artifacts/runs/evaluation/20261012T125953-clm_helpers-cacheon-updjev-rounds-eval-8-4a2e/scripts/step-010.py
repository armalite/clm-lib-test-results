import json,glob,re
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
n1['body']+=' R4: board.md:3 Follow-up OPEN ALERT_TUNING.'
c['entries']=[n1]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'WARN|ERROR|FATAL|OOM|restart|cert|pool|429|dns|disk|lag',l,re.I):print(f.split('/')[-1],i,l.strip()[:150])