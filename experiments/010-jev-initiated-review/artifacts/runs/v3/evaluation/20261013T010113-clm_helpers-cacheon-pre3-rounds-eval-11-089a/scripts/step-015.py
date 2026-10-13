import glob
print(open('/task/fixtures/round-03/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if any(k in l for k in ('ERROR','WARN','error','fail')):
            print(f.split('/')[-1],i,l.strip()[:150])