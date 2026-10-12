import json,glob,re
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if 'slow query' in l: continue
        print(f.split('/')[-1],i,l.strip()[:150])
