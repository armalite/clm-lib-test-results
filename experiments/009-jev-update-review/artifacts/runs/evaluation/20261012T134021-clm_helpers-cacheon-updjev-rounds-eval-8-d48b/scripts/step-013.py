import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|exhaust|cert|OOM|429|config|restart|dns|resolv|pool',l,re.I)]
    print(f.split('/')[-1],len(hits))
    for h in hits[:4]: print(' ',h[0],h[1][:150])
c=json.load(open('/task/workspace/context.json'))
n1=c['entries'][0]['body']+' R6: Thread A mitigated (round-06/board.md:3) via CHG-150 APPLIED pricing-svc (round-06/changes.md:4); Thread D DNS_RESOLUTION notify-worker ongoing (round-06/board.md:4) - verify vs CHG-113 pool_max=-4; CHG-147 log sampling irrelevant.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1}]},open('/task/workspace/context.json','w'))