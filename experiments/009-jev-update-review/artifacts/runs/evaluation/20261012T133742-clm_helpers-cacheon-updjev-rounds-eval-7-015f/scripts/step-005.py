import json,glob
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if 'ERROR' in l or 'error' in l.lower() and 'slow query' not in l:
            print(f.split('/')[-1],i,l.strip()[:160])
print(open('/task/fixtures/round-02/board.md').read())
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Round1: board empty. r1 changes.md:3 CHG-113 APPLIED ledger-svc build 7.35.5 sets db.pool_max=0 (suspect BAD_CONFIG_ROLLOUT); line4 CHG-114 checkout-api no config. Logs r1: only background WARN slow query in all 5 services (checkout,ledger,payments,search,shipping). R2: board.md:3 follow-up OPEN POSTMORTEM_DRAFT; changes.md:3 CHG-119 dashboards (irrelevant).'}]}
json.dump(c,open('/task/workspace/context.json','w'))