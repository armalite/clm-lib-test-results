import re,glob
print(open('/task/fixtures/round-05/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'slow query|INFO|/v1/health',l): continue
        print(f.split('/')[-1],i,l.strip()[:150])