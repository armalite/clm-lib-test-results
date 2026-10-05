import re
b='/task/fixtures/round-06/'
print(open(b+'board.md').read())
for s in ['auth-svc','ledger-svc','payments-svc','search-api','shipping-svc']:
    L=open(b+'logs/'+s+'.log').read().splitlines()
    h=[i for i,l in enumerate(L,1) if re.search(r'lag|certificate|ERROR|error|429|pool|ttl',l,re.I)]
    print(s,len(h),h[:1],h[-1:], L[h[0]-1][:160] if h else '')