import json,re
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']+=' R8 logs: inventory pool exhausted (round-08/logs/inventory-svc.log:2,4,9,13); others only slow queries. R9: board.md:3 Follow-up OPEN RUNBOOK_UPDATE.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['inventory-svc','notify-worker','auth-svc','pricing-svc','payments-svc']:
    L=open(f'/task/fixtures/round-09/logs/{s}.log').read().splitlines()
    h=[(i+1,re.search(r'msg\W+([a-z ]+)',l).group(1) if re.search(r'msg\W+([a-z ]+)',l) else l[:60]) for i,l in enumerate(L) if re.search('WARN|ERROR',l) and 'slow query' not in l]
    print(s,h[:8])