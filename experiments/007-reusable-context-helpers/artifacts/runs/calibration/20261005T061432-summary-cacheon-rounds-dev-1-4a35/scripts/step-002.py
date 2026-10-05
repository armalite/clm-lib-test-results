import glob
for f in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  L=open(f).read().splitlines()
  print('==',f.split('/')[-1],len(L));print(L[0][:200])
  for i,l in enumerate(L,1):
    if any(k in l.lower() for k in ['warn','error','fail','429','exhaust','expire','lag','oom','disk']):print(i,l[:160])