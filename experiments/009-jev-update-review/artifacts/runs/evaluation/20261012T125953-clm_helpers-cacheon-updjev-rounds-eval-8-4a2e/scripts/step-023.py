import json,re
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1': e['body']+=' R8: board.md:3 Thread A resolved; board.md:4 Thread B revised DB_POOL_EXHAUSTED (supersedes cert); board.md:5 Thread D false alarm (drop DNS).'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for s in ['inventory-svc','notify-worker','auth-svc','pricing-svc','payments-svc']:
    L=open(f'/task/fixtures/round-08/logs/{s}.log').read().splitlines()
    h=[i+1 for i,l in enumerate(L) if re.search('WARN|ERROR',l)]
    print(s,h[:12],L[h[0]-1][:150] if h else '')