import glob
r='/task/fixtures/round-03/'
print(open(r+'board.md').read());print(open(r+'changes.md').read())
for f in sorted(glob.glob(r+'logs/*.log')):
  n=0
  for i,l in enumerate(open(f),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l:
      n+=1
      if n<=6: print(f.split('/')[-1],i,l.strip()[:140])
  print(f.split('/')[-1],'count',n)