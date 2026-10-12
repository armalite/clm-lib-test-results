import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    L=open(f).read().splitlines()
    errs=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|error|429|expired|miss',l)]
    print(f.split('/')[-1],len(errs))
    for i,l in errs[:3]+errs[-1:]: print(' ',i,l[:150])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R3: board.md:3 Thread B CACHE_STAMPEDE payments-svc ongoing. changes.md:3 CHG-124 APPLIED retry budget GETs=1.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))