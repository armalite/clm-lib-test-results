import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|FATAL|429|pool|cert|dns|OOM|disk|lag|restart',l,re.I):
            print(f.split('/')[-1],i,l.strip()[:130])
n1='R1: board empty. CHG-109 APPLIED TLS ticket rotation hourly (round-01/changes.md:3); CHG-113 APPLIED notify-worker 8.20.0 db.pool_max=-4 (round-01/changes.md:4) suspect BAD_CONFIG_ROLLOUT, no board thread yet; CHG-114 APPLIED inventory-svc 8.20.0 (round-01/changes.md:5). R2: round-02/changes.md:3 CHG-114 id reused, PROPOSED HPA (not applied). R2 logs quiet. R3: Thread A MEMORY_LEAK pricing-svc+auth-svc ongoing (round-03/board.md:3); Thread B suspected CERT_EXPIRED inventory-svc ongoing (round-03/board.md:4, suspected only); CHG-124 APPLIED retry budget GET=1 (round-03/changes.md:3).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1}]},open('/task/workspace/context.json','w'))