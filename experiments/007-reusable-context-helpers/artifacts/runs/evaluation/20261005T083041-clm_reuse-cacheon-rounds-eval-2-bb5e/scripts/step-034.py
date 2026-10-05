import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-12/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-12/logs/*')):
  ls=[i for i,l in enumerate(open(f),1) if re.search('SERVFAIL|validation|certificate|heap|restart|ERROR',l)]
  print(f.split('/')[-1],len(ls),ls[:1],ls[-1:])
