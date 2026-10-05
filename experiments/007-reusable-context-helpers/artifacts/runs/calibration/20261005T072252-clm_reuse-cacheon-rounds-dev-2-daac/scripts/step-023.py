import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    L=[(i+1,l) for i,l in enumerate(open(f)) if re.search(r'ERROR|error|429|FATAL',l)]
    print(f.split('/')[-1],len(L),L[0][0] if L else '',L[-1][0] if L else '')
    if L: print(' ',L[0][1][:200].strip())