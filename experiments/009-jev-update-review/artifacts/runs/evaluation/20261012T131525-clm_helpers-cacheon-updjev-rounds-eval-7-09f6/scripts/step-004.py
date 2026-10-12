import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|CRIT',l) or ('WARN' in l and 'slow' not in l.lower()): print(f.split('/')[-1],i,l.strip()[:150])
print(open('/task/fixtures/round-02/board.md').read())
n='R1: CHG-113 APPLIED round-01/changes.md:3 ledger-svc build 7.35.5 sets db.pool_max=0 (suspect BAD_CONFIG_ROLLOUT). CHG-114 checkout-api no config (r1 changes.md:4). R1 logs noise only. Svcs: checkout-api, ledger-svc, payments-svc, search-api, shipping-svc. R2: board.md:3 followup OPEN POSTMORTEM_DRAFT; CHG-119 dashboards (irrelevant).'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))