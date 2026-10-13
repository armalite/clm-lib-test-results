import glob,re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|error|FATAL|429|SERVFAIL|batch',l)]
  print(f.split('/')[-1],len(L),L[:2],L[-1:] if L else '')