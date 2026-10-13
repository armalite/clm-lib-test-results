import glob
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=[i for i,l in enumerate(open(f),1) if ('ERROR' in l or 'WARN' in l)]
  print(f.split('/')[-1],n[:12])
  for i,l in enumerate(open(f),1):
    if i in n[:1]:print(' ',l.rstrip()[:160])