import re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    L=open(f).read().splitlines();h=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|FATAL|CRIT|429|exhaust|expired|NXDOMAIN|SERVFAIL|lag|OOM|disk|batch|heap',l,re.I)]
    print(f.split('/')[-1],len(h),h[:1],h[-1:],L[h[0]-1][:160] if h else '')