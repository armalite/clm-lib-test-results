import glob,re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=f.split('/')[-1];c=0
  for i,l in enumerate(open(f),1):
    if re.search(r'ERR|error|429|expired|fail',l,re.I):
      c+=1
      if c<=3:print(n,i,l.rstrip()[:160])
  print(n,'count',c)