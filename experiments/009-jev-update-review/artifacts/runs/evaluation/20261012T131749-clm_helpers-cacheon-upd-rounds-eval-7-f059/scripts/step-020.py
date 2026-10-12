import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    hits=[]
    for i,l in enumerate(open(f),1):
        if re.search(r'WARN|ERROR|error|429|disk|memory|pool',l) and 'slow query' not in l: hits.append((i,l.strip()[:150]))
    print(f.split('/')[-1],len(hits))
    for h in hits[:3]: print(h)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R7: board empty; changes.md:3 CHG-154 PROPOSED (ignore).'
json.dump(c,open('/task/workspace/context.json','w'))