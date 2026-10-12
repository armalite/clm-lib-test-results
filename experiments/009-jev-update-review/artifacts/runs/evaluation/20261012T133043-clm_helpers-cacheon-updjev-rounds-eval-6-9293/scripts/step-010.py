import os
d='/task/fixtures/round-03/logs/'
for s in sorted(os.listdir(d)):
  L=open(d+s).read().splitlines()
  print(s,len(L));[print(' ',l[:150]) for l in L[:3]]