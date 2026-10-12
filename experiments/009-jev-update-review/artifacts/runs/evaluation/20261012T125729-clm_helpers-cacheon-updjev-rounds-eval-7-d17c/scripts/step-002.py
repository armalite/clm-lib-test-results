import os,json
b='/task/fixtures/round-01/logs/'
for x in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+x)):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l: print(x,i+1,l.strip()[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md:3 CHG-113 APPLIED ledger-svc build 7.35.5 sets db.pool_max=0 (suspect BAD_CONFIG_ROLLOUT); :4 CHG-114 checkout-api no config. Logs r1: slow query WARNs everywhere (noise).'}]}
json.dump(c,open('/task/workspace/context.json','w'))