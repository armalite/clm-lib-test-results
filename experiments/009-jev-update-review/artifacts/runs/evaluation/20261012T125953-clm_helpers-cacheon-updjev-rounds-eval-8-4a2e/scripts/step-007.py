import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|restart|OOM|cert|x509|pool|429|dns',l,re.I): print(f.split('/')[-1],i,l.strip()[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: CHG-109 APPLIED TLS ticket rotation (r1 changes.md:3); CHG-113 APPLIED notify-worker 8.20.0 db.pool_max=-4 (r1 changes.md:4, suspect BAD_CONFIG_ROLLOUT); CHG-114 inventory no config (r1 changes.md:5). R2: pricing-svc heap WARNs rss 2200-3660 (round-02/logs/pricing-svc.log:6,7,55,66,83). R3: board.md:3 Thread A MEMORY_LEAK pricing-svc+auth-svc ongoing; board.md:4 Thread B inventory-svc suspected CERT_EXPIRED ongoing; changes.md:3 CHG-124 retry budget=1 (minor).'}]}
json.dump(c,open('/task/workspace/context.json','w'))