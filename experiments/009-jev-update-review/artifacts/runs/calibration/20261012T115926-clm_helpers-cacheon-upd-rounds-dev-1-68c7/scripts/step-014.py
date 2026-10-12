import json,collections,glob,os
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    c=collections.Counter();ex={}
    for i,l in enumerate(open(f),1):
        L=l.lower()
        if ('warn' in L or 'error' in L) and 'slow' not in L:
            k=' '.join(l.split()[3:6])[:40];c[k]+=1;ex.setdefault(k,(i,l.strip()[:120]))
    for k,v in c.items(): print(os.path.basename(f),v,ex[k][0],ex[k][1])
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace(' R3 non-slow lines in spill/s10.obs.txt.',' R3 logs: auth-svc.log:7, search-api.log:1 pool exhausted.')+' R4: board.md:3 Thread B CACHE_STAMPEDE payments-svc ongoing; changes.md:3 CHG-133 TLS ticket rotation APPLIED.'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))