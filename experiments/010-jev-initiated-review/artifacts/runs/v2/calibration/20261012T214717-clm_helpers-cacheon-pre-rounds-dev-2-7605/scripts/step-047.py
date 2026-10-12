import glob,re
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  hits={}
  for i,l in enumerate(open(f),1):
    for k in ['429','max_inflight','certificate','SERVFAIL','ERROR','restart','OOM']:
      if k in l: hits.setdefault(k,[]).append(i)
  print(f.split('/')[-1],{k:v[:6] for k,v in hits.items()})