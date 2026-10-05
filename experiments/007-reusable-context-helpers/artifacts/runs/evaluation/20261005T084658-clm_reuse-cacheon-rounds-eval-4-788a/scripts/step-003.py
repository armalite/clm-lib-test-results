import ctx
ctx.keep_notes('R1: inventory-svc db pool exhausted WARN round-01/logs/inventory-svc.log:5,9,28,30,45,52. slow query WARNs = noise. board r1 empty. changes r1: CHG-113 APPLIED search-api cache.ttl_s=-1 (round-01/changes.md:4); CHG-114 auth-svc no cfg; CHG-107 PROPOSED.')
import os,glob
for f in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'cache' in l.lower() or 'ttl' in l.lower()) and 'slow query' not in l: print(os.path.basename(f),i,l.strip()[:150])