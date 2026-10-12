import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['notify-worker','inventory-svc','payments-svc']:
    L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
    h=[i+1 for i,l in enumerate(L) if re.search('ERROR|exhaust|config|restart|OOM',l) and 'slow query' not in l]
    print(s,h[:15])
    if h: print(L[h[0]-1][:200])