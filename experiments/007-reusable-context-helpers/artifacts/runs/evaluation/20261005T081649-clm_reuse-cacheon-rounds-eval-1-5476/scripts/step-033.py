import re
b='/task/fixtures/round-11/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in ['auth-svc','search-api','shipping-svc','payments-svc','ledger-svc']:
    L=[(i,l) for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search(r'ERROR|cert|config|lag|429|pool',l,re.I)]
    print(s,len(L),[i for i,_ in L][:3],[i for i,_ in L][-2:]);
    if L:print(L[0][1].strip()[:200])