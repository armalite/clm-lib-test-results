import re,glob
for f in sorted(glob.glob('/task/fixtures/round-03/**/*',recursive=True)):
  if f.endswith('.md'):
    print(f);print(open(f).read())
  elif f.endswith('.log'):
    L=open(f).read().splitlines();h=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|FATAL|CRIT|429|exhaust|expired|NXDOMAIN|lag|OOM|disk|batch',l,re.I)]
    print(f,len(h))
    for x in h[:3]+h[-1:]:print(x)
