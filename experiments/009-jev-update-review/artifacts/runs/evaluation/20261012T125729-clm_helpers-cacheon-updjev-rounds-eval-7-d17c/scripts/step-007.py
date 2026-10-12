import json,glob
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if 'ERROR' in l or '429' in l or 'pool' in l.lower():
      print(f.split('/')[-1],i,l.strip()[:140])
n='R1: changes.md:3 CHG-113 APPLIED ledger-svc build 7.35.5 sets db.pool_max=0 (suspect BAD_CONFIG_ROLLOUT, no errors yet); slow query WARNs noise. R2: board.md:3 OPEN POSTMORTEM_DRAFT; shipping 429 tax-provider logs lines 7,22,35. R3: board.md:3 Thread A UPSTREAM_RATE_LIMIT shipping-svc+search-api ongoing; board:4 OPEN DATA_BACKFILL; :5 OPEN CAPACITY_REVIEW; changes:3 CHG-124 TLS ticket rotation (watch CERT).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))