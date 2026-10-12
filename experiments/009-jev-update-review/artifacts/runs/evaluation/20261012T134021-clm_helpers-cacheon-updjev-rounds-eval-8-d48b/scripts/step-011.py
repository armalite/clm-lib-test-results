import json,re,glob
print(open('/task/fixtures/round-05/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|exhaust|cert|OOM|429|config|restart',l,re.I)]
    print(f.split('/')[-1],len(hits))
    for h in hits[:3]: print(' ',h[0],h[1][:140])
c=json.load(open('/task/workspace/context.json'))
n1=c['entries'][0]['body']+' R5: CHG-135 APPLIED log sampling health 1% (round-05/changes.md:3), irrelevant.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1}]},open('/task/workspace/context.json','w'))