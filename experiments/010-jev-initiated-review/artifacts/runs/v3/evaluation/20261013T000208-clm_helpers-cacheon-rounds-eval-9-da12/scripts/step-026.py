import re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    ls=[(i+1,l.strip()) for i,l in enumerate(open(f)) if not re.search(r'slow.query|INFO',l)]
    print(f.split('/')[-1],len(ls),[x[0] for x in ls][:40])
    for x in ls[:2]: print(' ',x[0],x[1][:150])