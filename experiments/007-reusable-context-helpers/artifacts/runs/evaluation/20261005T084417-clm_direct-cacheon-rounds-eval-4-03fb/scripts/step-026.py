import re,glob
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
    hits={}
    for i,l in enumerate(open(f),1):
        for k in ['429','pool','ttl_s','memory','miss','cert','DNS','disk','lag']:
            if k.lower() in l.lower():hits.setdefault(k,[]).append(i)
    print(f.split('/')[-1],hits)