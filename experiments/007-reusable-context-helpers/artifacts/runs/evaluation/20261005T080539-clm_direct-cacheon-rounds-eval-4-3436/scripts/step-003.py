import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. slow query WARNs = noise. inventory-svc db pool exhausted WARN round-01/logs/inventory-svc.log:5,9,28,30,45,52. changes r01: CHG-113 APPLIED search-api 8.23.7 sets cache.ttl_s=-1 (round-01/changes.md:4, suspect BAD_CONFIG_ROLLOUT); CHG-114 auth-svc no config; CHG-107 PROPOSED only. Next: advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-01/changes.md').read().splitlines()[3])