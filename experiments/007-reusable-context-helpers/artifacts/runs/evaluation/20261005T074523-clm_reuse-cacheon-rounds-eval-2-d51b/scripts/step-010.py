import glob,re
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=f.split('/')[-1]
  c=0
  for i,l in enumerate(open(f),1):
    if re.search(r'slow query|INFO|/v1/health',l): continue
    c+=1
    if c<=6: print(n,i,l.rstrip()[:160])
  print(n,'nonnoise',c)