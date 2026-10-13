import re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    L=[(i+1,l.strip()) for i,l in enumerate(open(f)) if 'slow query' not in l and 'INFO' not in l]
    print(f.split('/')[-1],len(L),L[:2],L[-1:] if L else '')