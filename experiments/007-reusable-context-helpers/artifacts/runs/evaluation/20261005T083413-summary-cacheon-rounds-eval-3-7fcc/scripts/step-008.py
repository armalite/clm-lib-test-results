import glob
b='/task/fixtures/round-03/'
print(open(b+'board.md').read()[:800])
print(open(b+'changes.md').read()[:800])
for p in sorted(glob.glob(b+'logs/*')):
  n=0
  print(p.split('/')[-1],'L1',open(p).readline()[:130].strip())
  for i,l in enumerate(open(p),1):
    if 'slow' not in l and 'INFO' not in l and 'info' not in l:
      n+=1
      if n<=3: print(p.split('/')[-1],i,l[:130].strip())
  print(p.split('/')[-1],'count',n)
