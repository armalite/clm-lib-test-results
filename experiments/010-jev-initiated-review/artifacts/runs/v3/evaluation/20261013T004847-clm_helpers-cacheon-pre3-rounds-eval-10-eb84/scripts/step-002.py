import os
b='/task/fixtures/round-01/logs/'
for f in sorted(os.listdir(b)):
  L=open(b+f).read().splitlines()
  print(f,len(L))
  for i,l in enumerate(L,1):
    if any(k in l.lower() for k in ('error','warn','fail','429','timeout')):print(i,l[:160])