import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*')):
  L=[(i+1,l.strip()) for i,l in enumerate(open(f)) if not re.search('heartbeat|health ok|gc cycle|slow query|request ok',l)]
  print(f.split('/')[-1],len(L))
  for x in L[:4]+L[-2:]: print(' ',x[0],x[1][:150])