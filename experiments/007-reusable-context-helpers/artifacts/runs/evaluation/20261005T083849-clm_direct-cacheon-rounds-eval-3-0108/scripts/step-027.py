import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-09/'+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|429|heap|disk|FATAL|restart',l,re.I)]
  print(f.split('/')[-1],len(L));[print(i,l[:160]) for i,l in L[:3]+L[-1:]]