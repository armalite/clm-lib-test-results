import os,re
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  e=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|error|level=error|"error"',l) and 'slow' not in l]
  print(f,len(e),[x[0] for x in e[:1]],[x[0] for x in e[-1:]])
  if e: print('  ',e[0][1][:160])
  else: print(' first',L[0][:160])
