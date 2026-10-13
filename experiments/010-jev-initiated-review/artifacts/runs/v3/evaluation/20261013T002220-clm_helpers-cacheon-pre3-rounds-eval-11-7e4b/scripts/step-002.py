import glob
for p in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  L=open(p).read().splitlines()
  print(p.split('/')[-1],L[0][:160])
  for i,l in enumerate(L,1):
    if any(k in l.lower() for k in ['error','warn','fail','429','timeout','batch']):print(i,l[:160])