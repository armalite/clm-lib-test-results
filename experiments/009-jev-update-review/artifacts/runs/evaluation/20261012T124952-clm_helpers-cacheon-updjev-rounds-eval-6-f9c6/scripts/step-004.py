import os,json
b='/task/fixtures/round-02/logs/'
for f in sorted(os.listdir(b)):
 for i,l in enumerate(open(b+f),1):
  if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l:print(f,i,l.strip()[:130])
n='R1: no board. ledger-svc 429 upstream=fx-rates round-01/logs/ledger-svc.log:11-62. R2: board.md:3 Thread A UPSTREAM_RATE_LIMIT ledger-svc+inventory-svc ongoing; board.md:4 OPEN CAPACITY_REVIEW. changes.md:4 CHG-120 APPLIED pricing-svc feature.batch_size=0 (BAD_CONFIG candidate); :5 CHG-121 payments no config.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))