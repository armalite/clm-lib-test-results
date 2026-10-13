import glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if any(k in l for k in ['ERROR','FATAL','error','429','SERVFAIL','cert','inflight']):print(p.split('/')[-1],i,l.rstrip()[:150])