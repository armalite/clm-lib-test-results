import json
c=json.load(open('/task/workspace/context.json'))
b="Round1: board empty. 5 services (checkout-api,pricing-svc,ledger-svc,inventory-svc,search-api) only WARN slow query noise. round-01/changes.md:3 CHG-110 APPLIED retry GET=1; :4 CHG-113 APPLIED 3.22.4 pricing-svc cache.ttl_s=-1 (suspect BAD_CONFIG_ROLLOUT); :5 CHG-114 APPLIED 3.22.4 ledger-svc no config. Round2: board.md follow-up OPEN CAPACITY_REVIEW; changes.md CHG-115 APPLIED retry GET=1. round-02 checkout-api logs all INFO (need grep ERROR/WARN other services r2). Next: grep r2 logs non-INFO, then advance."
c['entries']=[{'id':'n1','role':'note','body':b}]
json.dump(c,open('/task/workspace/context.json','w'))
import glob
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if ' INFO ' not in l and 'slow query' not in l: print(f.split('/')[-1],i,l.strip()[:140])