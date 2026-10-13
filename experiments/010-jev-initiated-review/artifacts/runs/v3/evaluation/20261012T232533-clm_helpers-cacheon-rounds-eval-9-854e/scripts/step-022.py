import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|error|FATAL|CRIT',l)]
  print(f.split('/')[-1],len(L),L[0][0] if L else '',L[-1][0] if L else '')
  for i,l in L[:2]:print(' ',i,l[:200])