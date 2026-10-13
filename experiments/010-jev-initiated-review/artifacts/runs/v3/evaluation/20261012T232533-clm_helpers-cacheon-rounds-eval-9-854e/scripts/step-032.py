import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERR|error|fail',l,re.I)]
  print(f.split('/')[-1],len(L),L[:2],L[-1:] )