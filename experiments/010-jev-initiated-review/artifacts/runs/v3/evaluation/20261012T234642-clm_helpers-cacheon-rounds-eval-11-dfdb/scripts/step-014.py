import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-05/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  hits=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|error|fail|429|FATAL',l)]
  print(f.split('/')[-1],len(hits))
  for i,l in hits[:4]:print(' ',i,l[:150])