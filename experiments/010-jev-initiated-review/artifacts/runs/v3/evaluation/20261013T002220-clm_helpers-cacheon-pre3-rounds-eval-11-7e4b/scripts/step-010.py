import glob
b='/task/fixtures/round-03/'
for i,l in enumerate(open(b+'board.md'),1):print('board',i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if any(k in l for k in ('ERROR','FATAL','429','error','fail','CRIT')):print(f.split('/')[-1],i,l.rstrip()[:150])