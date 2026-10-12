import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log'))+['/task/fixtures/round-05/board.md']:
  for i,l in enumerate(open(f),1):
    if f.endswith('.md') or (re.search('ERROR|WARN|error|warn',l) and 'slow query' not in l): print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4')]
c['entries'].append({'id':'n5','role':'note','body':'R5: changes.md:3 CHG-137 PROPOSED HPA search (not applied, irrelevant).'})
json.dump(c,open('/task/workspace/context.json','w'))