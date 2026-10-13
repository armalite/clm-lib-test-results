import glob
print(open('/task/fixtures/round-10/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*.log')):
  L=[i+1 for i,l in enumerate(open(f)) if 'ERROR' in l or 'error' in l.lower() and '429' in l]
  print(f.split('/')[-1],len(L),L[:3],L[-3:])
  for i,l in enumerate(open(f)):
    if i+1 in L[:1]: print(l.strip()[:200])