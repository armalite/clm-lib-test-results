import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*')):
  ls=[(i,l) for i,l in enumerate(open(f),1) if re.search('ERROR|error|FATAL|429|SERVFAIL|expired',l)]
  print(f.split('/')[-1],len(ls),ls[0][0] if ls else '',ls[-1][0] if ls else '')
  if ls: print(ls[0][1][:200])