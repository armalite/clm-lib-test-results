import glob,json
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if ('WARN' in l or 'ERROR' in l or 'error' in l) and 'slow query' not in l: print(f.split('/')[-1],i,l.strip()[:160])
print(open('/task/fixtures/round-02/board.md').read())
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R2: board.md:3 follow-up OPEN POSTMORTEM_DRAFT; changes.md:3 CHG-119 dashboards (irrelevant).'
json.dump(c,open('/task/workspace/context.json','w'))