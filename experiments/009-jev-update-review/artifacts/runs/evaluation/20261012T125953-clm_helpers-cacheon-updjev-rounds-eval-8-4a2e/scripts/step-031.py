import json,re
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']=e['body'].replace(' Next: advance to R11.','')+' R11: board.md:3 Thread B mitigated; board.md:4 Thread C pods restarting; changes.md:3 CHG-182 minor.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['notify-worker','inventory-svc','payments-svc','auth-svc','pricing-svc']:
    L=open(f'/task/fixtures/round-11/logs/{s}.log').read().splitlines()
    h=[i+1 for i,l in enumerate(L) if re.search('ERROR|WARN|exhaust|config',l)]
    print(s,h[:12]);
    if h: print(L[h[0]-1][:160])