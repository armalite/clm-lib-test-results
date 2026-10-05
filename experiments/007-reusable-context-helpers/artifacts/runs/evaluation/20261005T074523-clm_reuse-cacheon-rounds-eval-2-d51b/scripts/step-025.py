import re,glob
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  L=[(i+1,l.strip()) for i,l in enumerate(open(f)) if not re.search(r'slow query|INFO|/v1/health',l)]
  print(f.split('/')[-1],len(L))
  for x in L[:3]+L[-1:]: print(' ',x[0],x[1][:150])