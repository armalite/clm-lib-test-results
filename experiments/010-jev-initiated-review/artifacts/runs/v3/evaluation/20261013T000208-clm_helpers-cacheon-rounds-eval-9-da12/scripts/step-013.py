import re,glob
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if not re.search(r'slow.query|INFO',l):
      n+=1
      if n<=4: print(f.split('/')[-1],i,l.strip()[:150])
  print(f.split('/')[-1],'count',n)