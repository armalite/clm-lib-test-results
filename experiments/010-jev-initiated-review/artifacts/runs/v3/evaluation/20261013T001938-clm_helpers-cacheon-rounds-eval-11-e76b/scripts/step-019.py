import re,glob
d='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(d+f),1): print(f,i,l.rstrip())
r=re.compile(r'ERROR|FATAL|CRIT|429|exhaust|expired|NXDOMAIN|SERVFAIL|lag|OOM|disk|batch',re.I)
for f in sorted(glob.glob(d+'logs/*')):
    h=[(i,l) for i,l in enumerate(open(f),1) if r.search(l)]
    if h: print(f.split('/')[-1],len(h),h[0][0],h[-1][0],h[0][1][:160])
