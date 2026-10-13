import json,glob
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*')):
  for i,l in enumerate(open(f),1):
    if 'slow query' not in l and ' INFO ' not in l:print(f.split('/')[-1],i,l.rstrip()[:140])
n1='Round01: board empty. logs only WARN slow query (noise). round-01/changes.md:3 CHG-110 APPLIED retry GETs=1; :4 CHG-113 APPLIED build 3.22.4 pricing-svc cache.ttl_s=-1 (suspicious BAD_CONFIG_ROLLOUT); :5 CHG-114 APPLIED 3.22.4 ledger-svc no config changes.'
n2='Round02: round-02/board.md:3 Follow-up OPEN CAPACITY_REVIEW. round-02/changes.md:3 CHG-115 APPLIED retry GETs=1. Logs: scan non-INFO/non-slow-query lines (see next obs).'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1},{'id':'n2','role':'note','body':n2}]}
json.dump(c,open('/task/workspace/context.json','w'))