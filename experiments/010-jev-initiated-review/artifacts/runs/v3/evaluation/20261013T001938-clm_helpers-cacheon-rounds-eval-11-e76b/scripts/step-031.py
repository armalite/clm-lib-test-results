import re,glob
d='/task/fixtures/round-11/'
print(open(d+'board.md').read())
for f in sorted(glob.glob(d+'logs/*')):
    L=[(i+1,l) for i,l in enumerate(open(f)) if re.search(r'ERROR|FATAL|CRIT|429|exhaust|expired|NXDOMAIN|SERVFAIL|lag|OOM|disk|batch|heap',l)]
    print(f.split('/')[-1],len(L),L[0][0] if L else '',L[-1][0] if L else '',L[0][1][:160] if L else '')