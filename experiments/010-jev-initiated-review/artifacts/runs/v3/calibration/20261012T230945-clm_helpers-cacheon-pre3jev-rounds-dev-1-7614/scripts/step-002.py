import glob
for p in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  L=open(p).readlines()
  print(p.split('/')[-1],L[0][:160].strip())
  for i,l in enumerate(L,1):
    if any(k in l for k in ('ERROR','WARN','error','warn')):print(i,l[:150].strip())