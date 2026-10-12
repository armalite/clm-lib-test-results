import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    s=f.split('/')[-1]
    hits={}
    for i,l in enumerate(open(f),1):
        if 'slow query' in l: continue
        if re.search(r'WARN|ERROR|FATAL|restart|level=(warn|error)',l,re.I):
            k=re.sub(r'[0-9]+','#',l)[:90]
            hits.setdefault(k,[]).append(i)
    for k,v in hits.items(): print(s,v[:12],k.strip()[:90])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))