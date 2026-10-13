import os,re
d='/task/fixtures/round-06/logs/'
for f in sorted(os.listdir(d)):
  L=open(d+f).read().splitlines()
  hits=[(i,l) for i,l in enumerate(L,1) if re.search(r'(?i)error|fail|expired|disk|pool|429|oom|lag',l)]
  print(f,len(L),len(hits))
  for i,l in hits[:4]: print(' ',i,l[:150])
