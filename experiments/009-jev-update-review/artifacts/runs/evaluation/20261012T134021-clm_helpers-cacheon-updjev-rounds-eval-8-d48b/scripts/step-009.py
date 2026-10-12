import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|WARN|exhaust|cert|OOM|memory|429|config',l,re.I)]
    print(f.split('/')[-1],len(hits))
    for h in hits[:3]: print(' ',h[0],h[1][:150])
c=json.load(open('/task/workspace/context.json'))
n1=c['entries'][0]['body'].replace(' Next: advance to R4.','')+' R4: ALERT_TUNING follow-up OPEN (round-04/board.md:3).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1}]},open('/task/workspace/context.json','w'))