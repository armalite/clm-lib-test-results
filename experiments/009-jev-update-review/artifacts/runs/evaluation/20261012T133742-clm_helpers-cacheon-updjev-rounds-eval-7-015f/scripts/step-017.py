import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'429|used_pct|pool|cert|expired|ERROR',l,re.I) and 'slow' not in l: print(f.split('/')[-1],i,l.strip()[:140])
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
b=d['entries'][0]['body'].replace(' Round 5 done; next: advance.','')
d['entries'][0]['body']=b+' R6: board.md:3 Thread A now MITIGATED; changes.md:3 CHG-150 APPLIED shipping-svc mitigation.'
json.dump(d,open('/task/workspace/context.json','w'))