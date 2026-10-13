import glob
for f in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  L=open(f).read().splitlines()
  print(f.split('/')[-1],len(L))
  for i,l in enumerate(L,1):
    if any(k in l for k in ('ERROR','WARN','error','warn')):print(i,l[:160])