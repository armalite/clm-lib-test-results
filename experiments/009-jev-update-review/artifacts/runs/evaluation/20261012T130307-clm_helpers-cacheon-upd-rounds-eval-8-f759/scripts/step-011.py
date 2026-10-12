import json,glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if 'error' in l.lower():
      print(f.split('/')[-1],i,l.strip()[:130]);n+=1
      if n>=2:break
b='R1: board empty. changes.md:3 CHG-109 APPLIED TLS ticket rotation hourly; :4 CHG-113 APPLIED build 8.20.0 notify-worker sets db.pool_max=-4 (invalid config -> watch BAD_CONFIG_ROLLOUT); :5 CHG-114 inventory-svc no config. R2: nothing. R3: board.md:3 Thread A MEMORY_LEAK confirmed pricing-svc, also auth-svc, ongoing; board.md:4 Thread B inventory-svc suspected CERT_EXPIRED ongoing; changes.md:3 CHG-124 APPLIED retry budget GET=1. R4: board.md:3 follow-up OPEN ALERT_TUNING. R5: changes.md:3 CHG-135 APPLIED health log sampling 1% (irrelevant).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))