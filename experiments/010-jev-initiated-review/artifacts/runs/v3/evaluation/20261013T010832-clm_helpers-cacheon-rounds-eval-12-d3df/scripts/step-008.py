import re,glob
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob(b+'logs/*')):
    for i,l in enumerate(open(p),1):
        if not re.search(r'slow query|request ok|heartbeat|gc |health ok',l,re.I):print(p.split('/')[-1],i,l.rstrip()[:120])