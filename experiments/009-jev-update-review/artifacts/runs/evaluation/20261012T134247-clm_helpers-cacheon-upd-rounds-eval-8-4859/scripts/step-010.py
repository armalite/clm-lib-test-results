import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    s=f.split('/')[-1]
    hits={}
    for i,l in enumerate(open(f),1):
        if 'slow query' in l: continue
        if re.search(r'WARN|ERROR|FATAL|restart|OOM',l,re.I):
            k=re.sub(r'[0-9]+','#',l)[:90]
            hits.setdefault(k,[]).append(i)
    for k,v in hits.items(): print(s,v[:12],k.strip())
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' R4 board:3 follow-up OPEN ALERT_TUNING.'
json.dump(c,open('/task/workspace/context.json','w'))