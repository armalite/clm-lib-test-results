import glob
for f in ['/task/fixtures/round-03/board.md']+sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  for i,l in enumerate(open(f),1):
    if 'board' in f or any(k in l for k in ('ERROR','WARN','error','warn')):
      if 'slow query' in l: continue
      print(f.split('round-03/')[1],i,l.rstrip()[:150])