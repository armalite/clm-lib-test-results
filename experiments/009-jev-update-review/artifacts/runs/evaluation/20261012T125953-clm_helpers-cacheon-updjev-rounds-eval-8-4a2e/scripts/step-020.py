import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    hits={}
    for i,l in enumerate(open(f),1):
        for k in ['heap','pool exhausted','dns','cert','429','disk','lag','OOM','restart','ERROR']:
            if k.lower() in l.lower(): hits.setdefault(k,[]).append(i)
    print(f.split('/')[-1],{k:v[:10] for k,v in hits.items()})
print(open('/task/fixtures/round-07/board.md').read())
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))