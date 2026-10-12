import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    L=open(f).read().splitlines();e=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|error|429|FATAL',l) and 'slow' not in l]
    print(f.split('/')[-1],len(e),e[0][0] if e else '',e[-1][0] if e else '');
    if e: print(e[0][1][:220])