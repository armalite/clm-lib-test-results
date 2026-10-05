import json,re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
skip=re.compile(r'request ok|heartbeat|gc |health ok|slow query|heap',re.I)
for s in ['auth-svc','inventory-svc','ledger-svc','payments-svc','pricing-svc']:
    ls=[(i,l.strip()) for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if not skip.search(l)]
    print(s,len(ls),[i for i,_ in ls][:30])
    for i,l in ls[:2]:print(' ',i,l[:150])
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'].startswith('n')]
json.dump(d,open(p,'w'))