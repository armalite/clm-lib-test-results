import re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    L=open(f).read().splitlines()
    e=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|error|FATAL|level=err',l)]
    print(f.split('/')[-1],len(e))
    for i,l in e[:3]: print(' ',i,l[:200])
    if e: print('  lines',[i for i,_ in e])