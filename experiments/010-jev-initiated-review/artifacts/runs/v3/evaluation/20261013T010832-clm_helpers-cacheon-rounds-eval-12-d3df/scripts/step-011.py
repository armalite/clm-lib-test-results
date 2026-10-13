import re,glob
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
noise=re.compile(r'slow query|request ok|heartbeat|gc |health ok',re.I)
for f in sorted(glob.glob(b+'logs/*')):
  ls=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if not noise.search(l)]
  n=f.split('/')[-1]
  print(n,len(ls))
  for i,l in ls[:3]+ls[-2:]:print(' ',i,l[:150])