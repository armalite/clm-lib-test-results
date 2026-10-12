import json,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if 'ERROR' in l or 'error' in l.lower() and 'WARN' not in l:
      print(f.split('/')[-1],i,l.strip()[:150])
      break
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md:3 CHG-109 APPLIED TLS ticket rotation hourly; :4 CHG-113 APPLIED build 8.20.0 notify-worker sets db.pool_max=-4 (invalid config -> watch BAD_CONFIG_ROLLOUT); :5 CHG-114 inventory-svc no config. R2: nothing. R3: board.md:3 Thread A MEMORY_LEAK confirmed pricing-svc, also auth-svc, ongoing; board.md:4 Thread B inventory-svc suspected CERT_EXPIRED ongoing; changes.md:3 CHG-124 APPLIED retry budget GET=1.'}]}
json.dump(c,open('/task/workspace/context.json','w'))