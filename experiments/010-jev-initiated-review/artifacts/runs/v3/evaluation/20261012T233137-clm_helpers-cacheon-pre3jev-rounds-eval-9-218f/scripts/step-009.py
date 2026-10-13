import glob
b='/task/fixtures/round-03/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if any(k in l for k in ('ERROR','FATAL','429','SERVFAIL','inflight','pool','OOM','disk','lag')):
      print(f.split('/')[-1],i,l.strip()[:150])