import json,re
for s in ['inventory-svc','ledger-svc','notify-worker','pricing-svc','search-api']:
    L=open(f'/task/fixtures/round-03/logs/{s}.log').read().splitlines()
    hits=[(i+1,l[:150]) for i,l in enumerate(L) if re.search(r'ERROR|FATAL|CRIT|level=error',l,re.I)]
    print(s,len(hits))
    for h in hits[:4]: print(' ',h)
b=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
b=b.replace('R2 done; next: advance.','R3 board: Thread B CACHE_STAMPEDE inventory-svc ongoing round-03/board.md:3. CHG-126 PROPOSED ignore.')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]},open('/task/workspace/context.json','w'))