import glob
print(open('/task/fixtures/round-06/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if 'INFO' in l or 'slow' in l: continue
        print(f.split('/')[-1],i,l.strip()[:150])
