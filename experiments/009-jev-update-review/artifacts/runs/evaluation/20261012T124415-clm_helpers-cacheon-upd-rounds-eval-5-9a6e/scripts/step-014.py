import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|certificate|disk|pool|memory|429|dns',l,re.I) and 'slow query' not in l:
            print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+=' R5: board.md:3 OPEN CAPACITY_REVIEW.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))