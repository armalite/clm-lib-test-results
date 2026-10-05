import re
b='/task/fixtures/round-11/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for s in ['auth-svc','search-api','shipping-svc','ledger-svc','payments-svc']:
    hits=[i for i,l in enumerate(open(b+'logs/'+s+'.log'),1) if re.search(r'ERROR|WARN|cert|config|lag|tls',l,re.I) and 'INFO' not in l]
    print(s,len(hits),hits[:3],hits[-3:] if hits else '')