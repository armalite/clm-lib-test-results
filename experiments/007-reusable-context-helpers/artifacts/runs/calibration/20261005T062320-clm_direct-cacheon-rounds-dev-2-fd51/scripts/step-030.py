import re,glob
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
    hits=[]
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|error|429|cert|SERVFAIL|validation|OOM|memory',l,re.I):hits.append(i)
    print(f.split('/')[-1],len(hits),hits[:8])
    if hits:print(open(f).readlines()[hits[0]-1][:200])