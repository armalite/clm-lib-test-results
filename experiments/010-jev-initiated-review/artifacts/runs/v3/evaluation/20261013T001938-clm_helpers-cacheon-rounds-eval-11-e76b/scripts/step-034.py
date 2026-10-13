import re,glob
print(open('/task/fixtures/round-12/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-12/logs/*.log')):
    L=[i+1 for i,l in enumerate(open(f)) if re.search(r'ERROR|FATAL|429|SERVFAIL|batch|heap',l)]
    print(f.split('/')[-1],len(L),L[:1],L[-1:])
    if L: print(open(f).readlines()[L[0]-1][:200])