import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    L=open(f).read().splitlines()
    h=[i+1 for i,l in enumerate(L) if re.search(r'disk|used_pct|429|pool|cache|miss|expired|dns|oom|lag',l,re.I)]
    print(f.split('/')[-1],len(h),h[:8])
    if h: print(' ',L[h[0]-1][:200])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance to R8.','')+' R8: board.md:3 Thread B (CACHE_STAMPEDE, ongoing) now also payments-svc; board.md:4 OPEN RUNBOOK_UPDATE.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))