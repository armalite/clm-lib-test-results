import json,glob
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'error' in l.lower()) and 'slow query' not in l: print(f.split('/')[-1],i,l.strip()[:150])
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'R1: CHG-113 APPLIED round-01/changes.md:3 notify-worker build 7.58.1 sets db.pool_max=0 (suspect BAD_CONFIG_ROLLOUT). pricing-svc CERT_EXPIRED peer=bank-api round-01/logs/pricing-svc.log:8,10,13,22. R2 board: Thread A CERT_EXPIRED pricing-svc+search-api ongoing round-02/board.md:3; Thread D DNS_RESOLUTION pricing-svc ongoing (unverified, maybe false alarm) board.md:4; VENDOR_TICKET open board.md:5. CHG-118 PROPOSED ignore. Slow query WARNs = noise.'}]}
json.dump(c,open('/task/workspace/context.json','w'))