import os,re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  ls=open(b+'logs/'+f).read().splitlines()
  e=[(i,l) for i,l in enumerate(ls,1) if re.search('ERROR|error|FATAL',l)]
  if e: print(f,len(e),e[0][0],e[-1][0],e[0][1][:160])
  else: print(f,'0 errs',ls[0][:120])