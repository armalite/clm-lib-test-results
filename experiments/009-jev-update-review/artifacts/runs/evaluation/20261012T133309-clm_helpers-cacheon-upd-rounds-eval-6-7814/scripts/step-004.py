import os,json
b='/task/fixtures/round-02/logs/'
out=[]
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f),1):
    if ('ERROR' in l or 'WARN' in l or 'error' in l) and 'slow query' not in l:out.append(f'{f}:{i} {l.strip()[:100]}')
print(len(out));print('\n'.join(out[:35]))
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'R1: no board. slow query WARNs = noise. ledger-svc 429 fx-rates round-01/logs/ledger-svc.log:11-62. R2: board.md:3 Thread A UPSTREAM_RATE_LIMIT ledger-svc+inventory-svc ongoing; board.md:4 CAPACITY_REVIEW open. changes.md:4 CHG-120 APPLIED pricing-svc feature.batch_size=0 (suspect BAD_CONFIG); CHG-121 payments no cfg.'}]}
json.dump(c,open('/task/workspace/context.json','w'))