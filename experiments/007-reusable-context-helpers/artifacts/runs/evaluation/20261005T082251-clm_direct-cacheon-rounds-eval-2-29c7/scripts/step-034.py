import json,re
b='/task/fixtures/round-11/'
print(open(b+'board.md').read())
for s in ['inventory-svc','ledger-svc','pricing-svc','auth-svc','payments-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    hits=[i+1 for i,l in enumerate(L) if re.search(r'(?i)error|fail|servfail|restart|oom|429|disk|pool',l) and not re.search(r'request ok|heartbeat|health ok',l)]
    print(s,len(hits),hits[:12])
    if hits: print(L[hits[0]-1][:200])
p='/task/workspace/context.json'
d=json.load(open(p))
d['entries']=[e for e in d['entries'] if e['id'].startswith('n')]
json.dump(d,open(p,'w'))