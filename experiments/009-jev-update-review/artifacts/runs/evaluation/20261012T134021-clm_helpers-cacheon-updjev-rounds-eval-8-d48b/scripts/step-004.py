import json,glob,re
print(open('/task/fixtures/round-02/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|FATAL|CRIT|429|pool|cert|dns|OOM|disk|lag',l,re.I) and 'slow query' not in l:
            print(f.split('/')[-1],i,l.strip()[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md: CHG-109 APPLIED TLS ticket rotation hourly (round-01/changes.md:3); CHG-113 APPLIED notify-worker build 8.20.0 sets db.pool_max=-4 (round-01/changes.md:4) -> suspect BAD_CONFIG_ROLLOUT; CHG-114 APPLIED inventory-svc 8.20.0 no config (round-01/changes.md:5). R2: round-02/changes.md:3 reuses id CHG-114 as PROPOSED HPA raise for search tier (not applied; distinct record, does not alter r1 facts). Services: notify-worker,pricing-svc,auth-svc,payments-svc,inventory-svc.'}]}
json.dump(c,open('/task/workspace/context.json','w'))