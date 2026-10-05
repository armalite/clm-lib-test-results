import glob
b='/task/fixtures/round-04/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip()[:200])
for p in sorted(glob.glob(b+'logs/*')):
  n=0;s=p.split('/')[-1]
  print(s,'L1',open(p).readline()[:130].strip())
  for i,l in enumerate(open(p),1):
    if 'slow' not in l and 'INFO' not in l and 'info' not in l:
      n+=1
      if n<=3: print(s,i,l[:140].strip())
  print(s,'count',n)
