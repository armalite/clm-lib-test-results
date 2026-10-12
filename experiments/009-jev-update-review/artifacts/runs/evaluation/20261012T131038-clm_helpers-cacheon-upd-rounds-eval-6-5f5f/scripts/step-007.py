import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|429|cache|miss|pool|batch',l,re.I):
            print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]
c['entries'].append({'id':'n3','role':'note','body':'R3: board round-03/board.md:3 Thread B payments-svc CACHE_STAMPEDE ongoing (suspected). changes round-03/changes.md:3 CHG-124 APPLIED retry budget GETs=1.'})
json.dump(c,open('/task/workspace/context.json','w'))