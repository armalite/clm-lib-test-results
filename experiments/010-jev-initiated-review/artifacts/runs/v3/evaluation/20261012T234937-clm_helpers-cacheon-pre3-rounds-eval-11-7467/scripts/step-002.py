import glob
for f in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  L=open(f).read().splitlines()
  print(f.split('/')[-1],len(L))
  n=0
  for i,l in enumerate(L,1):
    if any(k in l.lower() for k in ['error','warn','fail','429','timeout','invalid']):
      n+=1
      if n<=4:print(i,l[:200])
  print('hits',n)