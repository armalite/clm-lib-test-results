import json,collections,glob,os
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    c=collections.Counter();ex={}
    for i,l in enumerate(open(f),1):
        if ('WARN' in l or 'ERROR' in l or 'level=warn' in l.lower() or 'level=error' in l.lower()) and 'slow' not in l:
            k=' '.join(l.split()[3:6])[:40];c[k]+=1;ex.setdefault(k,(i,l.strip()[:110]))
    for k,v in c.items(): print(os.path.basename(f),v,ex[k][0],ex[k][1])
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
json.dump(d,open('/task/workspace/context.json','w'))