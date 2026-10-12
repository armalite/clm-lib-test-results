import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|FATAL|CRIT|OOM|cert|x509',l,re.I):print(f.split('/')[-1],i,l.rstrip()[:150])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: CHG-109 APPLIED TLS ticket rotation (round-01/changes.md:3); CHG-113 APPLIED notify-worker db.pool_max=-4 (round-01/changes.md:4) suspect BAD_CONFIG_ROLLOUT, no errors seen yet; CHG-114 APPLIED inventory-svc 8.20.0 (round-01/changes.md:5). R2 nothing (CHG-114 PROPOSED dup id irrelevant).'},{'id':'n3','role':'note','body':'R3 board: A MEMORY_LEAK pricing-svc+auth-svc ongoing (round-03/board.md:3); B suspected CERT_EXPIRED inventory-svc ongoing (round-03/board.md:4). CHG-124 APPLIED retry budget=1 (round-03/changes.md:3).'}]}
json.dump(c,open('/task/workspace/context.json','w'))