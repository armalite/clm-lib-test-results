import json,re
L=open('/task/fixtures/round-08/logs/pricing-svc.log').read().splitlines()
for i,l in enumerate(L,1):
    if re.search(r'ERROR|WARN|fail|invalid|batch',l,re.I) and 'slow query' not in l: print(i,l[:160])
for s in ['payments-svc','ledger-svc']:
    L=open(f'/task/fixtures/round-08/logs/{s}.log').read().splitlines()
    print(s,[i for i,l in enumerate(L,1) if re.search(r'used_pct|rss_mb|heap',l)][:8])
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1']
e[0]['body']+='\nR8: board.md:3 Thread B cause revised DISK_PRESSURE (payments-svc); board.md:4 Thread C pricing-svc failures ongoing cause unknown.'
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))