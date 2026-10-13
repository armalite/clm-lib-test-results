import glob,re
for p in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  L=open(p).read().splitlines()
  print(p.split('/')[-1],L[0][:160])
  for i,l in enumerate(L,1):
    if re.search(r'WARN|ERR|FATAL|429|expired|NXDOMAIN|pool|lag|OOM|disk',l,re.I):print(i,l[:150])