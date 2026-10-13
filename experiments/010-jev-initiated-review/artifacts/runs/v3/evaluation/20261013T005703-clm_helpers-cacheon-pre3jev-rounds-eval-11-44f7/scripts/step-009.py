import re,glob
print(open('/task/fixtures/round-03/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  L=open(f).read().splitlines()
  e=[(i+1,l[:140]) for i,l in enumerate(L) if re.search('ERROR|WARN|429|error',l)]
  print(f.split('/')[-1],len(e))
  for x in e[:5]:print(x)