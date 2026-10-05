import ctx
ctx.reset('R1 notes: changes.md:3 CHG-113 APPLIED search-api cache.ttl_s=-1 (likely BAD_CONFIG_ROLLOUT later); CHG-114 auth-svc no cfg; CHG-107 PROPOSED. inventory-svc db pool exhausted WARNs round-01/logs/inventory-svc.log:5,9,28,30,45,52 (DB_POOL candidate). slow query WARNs everywhere = noise. board empty. ctx.py has load/save/reset(notes).')
import re
L=open('/task/fixtures/round-01/logs/search-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if 'slow query' not in l and ('WARN' in l or 'ERROR' in l):print(i,l[:150])