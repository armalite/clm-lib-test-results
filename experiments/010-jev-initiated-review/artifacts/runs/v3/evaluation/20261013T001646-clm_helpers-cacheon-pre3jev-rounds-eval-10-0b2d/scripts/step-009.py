import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-03/logs/*')):
  ls=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|error|FATAL|WARN',l) and 'slow' not in l]
  print(f.split('/')[-1],len(ls))
  for x in ls[:4]:print(x)