import re,glob
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|error|lag|WARN',l) and 'slow' not in l:
      n+=1
      if n<=3:print(f.split('/')[-1],i,l.rstrip()[:160])
  print(f.split('/')[-1],'count',n)