import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    hits=[]
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|WARN|429|error',l) and 'slow query' not in l: hits.append((i,l.strip()[:150]))
    print(f.split('/')[-1],len(hits))
    for h in hits[:4]: print(h)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R4: board.md:3 Thread B CACHE_STAMPEDE checkout-api ongoing (verify; CHG-113 pool_max=0 is ledger). changes.md:3 CHG-128 log sampling (irrelevant).'
json.dump(c,open('/task/workspace/context.json','w'))