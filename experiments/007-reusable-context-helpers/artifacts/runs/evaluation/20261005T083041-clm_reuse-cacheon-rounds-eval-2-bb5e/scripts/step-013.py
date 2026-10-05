import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for s in ['auth','inventory','ledger','payments','pricing']:
    L=open(b+'logs/'+s+'-svc.log').read().splitlines()
    print(s,len(L))
    seen=set()
    for i,l in enumerate(L,1):
        if re.search('ERROR|WARN|error|warn|restart|OOM|SERVFAIL|429',l):
            k=re.sub(r'[0-9]+','#',l)[30:90]
            if k not in seen:
                seen.add(k);print(i,l[:160])
