import json,glob
print(open('/task/fixtures/round-02/board.md').read())
for p in sorted(glob.glob('/task/fixtures/round-02/logs/*')):
  for i,l in enumerate(open(p),1):
    if 'slow query' not in l and ('ERROR' in l or 'WARN' in l or 'pool' in l.lower()): print(p.split('/')[-1],i,l[:140].rstrip())
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R2: changes.md:3 CHG-114 PROPOSED HPA search tier (not applied; note R1 CHG-114 id reused).'
json.dump(c,open('/task/workspace/context.json','w'))