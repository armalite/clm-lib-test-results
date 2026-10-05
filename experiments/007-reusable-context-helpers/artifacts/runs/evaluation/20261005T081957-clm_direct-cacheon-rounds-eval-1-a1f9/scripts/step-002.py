import os,json,glob
for p in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if ' INFO ' not in l and 'slow query' not in l: print(p.split('/')[-1],i,l.strip()[:140])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes: CHG-112 APPLIED TLS ticket rotation hourly; CHG-113 APPLIED build 4.51.3 auth-svc sets cache.ttl_s=-1 (round-01/changes.md:4, suspicious BAD_CONFIG); CHG-114 APPLIED shipping-svc no config. Services: shipping-svc auth-svc payments-svc ledger-svc search-api. Log fmt: ts LEVEL svc msg. slow query WARNs are noise.'}]}
json.dump(c,open('/task/workspace/context.json','w'))