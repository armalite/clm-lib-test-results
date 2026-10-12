import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|WARN|FATAL|error',l) and 'slow query' not in l:print(f.split('/')[-1],i,l.strip()[:200])
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1']
e.append({'id':'n2','role':'note','body':'R2: board.md:3 Follow-up OPEN POSTMORTEM_DRAFT. changes.md:3 CHG-119 APPLIED dashboards (irrelevant).'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))