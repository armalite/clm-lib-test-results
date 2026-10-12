import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
    s=f.split('/')[-1];d={}
    for i,l in enumerate(open(f),1):
        if re.search(r'WARN|ERROR|FATAL',l) and 'slow query' not in l:
            k=re.sub(r'[0-9]+','#',l)[:90];d.setdefault(k,[]).append(i)
    for k,v in d.items(): print(s,v[:12],k)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']=c['entries'][0]['body'].replace(' Next: advance to R6.','')+' R6 board:3 Thread A mitigated; board:4 Thread D DNS_RESOLUTION notify-worker ongoing. changes:4 CHG-150 APPLIED mitigation thread A pricing-svc; :3 CHG-147 irrelevant.'
json.dump(c,open('/task/workspace/context.json','w'))