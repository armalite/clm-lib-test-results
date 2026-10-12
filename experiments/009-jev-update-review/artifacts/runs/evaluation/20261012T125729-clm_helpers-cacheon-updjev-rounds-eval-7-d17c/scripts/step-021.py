import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|pool|429|disk|cert|DNS|memory|lag',l,re.I)]
    print(f.split('/')[-1],len(hits),hits[:8],L[hits[0]-1][:150] if hits else '')
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n=n.replace(' NEXT: advance to R8.','')+' R8: board:3 Thread B CACHE_STAMPEDE now checkout-api+payments-svc; board:4 OPEN RUNBOOK_UPDATE.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))