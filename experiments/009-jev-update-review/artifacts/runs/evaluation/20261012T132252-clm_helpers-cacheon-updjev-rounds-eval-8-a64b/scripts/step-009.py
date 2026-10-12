import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|FATAL|CRIT|OOM|cert|x509|pool',l,re.I):print(f.split('/')[-1],i,l.rstrip()[:140])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4 board: Follow-up OPEN ALERT_TUNING (round-04/board.md:3).'})
json.dump(c,open('/task/workspace/context.json','w'))