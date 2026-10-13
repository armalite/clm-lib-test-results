import re,glob
print(open('/task/fixtures/round-10/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*.log')):
    L=[(i+1,l) for i,l in enumerate(open(f)) if re.search('ERROR|WARN|FATAL|fail|429',l) and 'slow' not in l]
    print(f.split('/')[-1],len(L),[i for i,_ in L][:3],[i for i,_ in L][-2:])
    if L: print(L[0][1][:200])