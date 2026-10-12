import os,json
b='/task/fixtures/round-02/logs/'
print(os.listdir(b))
for f in sorted(os.listdir(b)):
 if 'pricing' in f or 'payments' in f:
  for i,l in enumerate(open(b+f),1):
   if 'ERROR' in l or 'batch' in l or 'WARN' in l:print(f,i,l.strip()[:120])
n='R1: no board. ledger-svc 429 upstream=fx-rates round-01/logs/ledger-svc.log:11-62. R2: board.md:3 Thread A UPSTREAM_RATE_LIMIT ledger-svc+inventory-svc ongoing; board.md:4 OPEN CAPACITY_REVIEW. changes.md:4 CHG-120 APPLIED pricing-svc feature.batch_size=0 (BAD_CONFIG candidate); :5 CHG-121 payments no config. R2 logs: 429 fx-rates inventory-svc.log:18-86, ledger-svc.log:6-71.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))