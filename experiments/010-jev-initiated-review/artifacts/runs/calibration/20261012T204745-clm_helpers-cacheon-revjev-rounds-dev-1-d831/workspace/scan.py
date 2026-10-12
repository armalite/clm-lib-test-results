import os,sys
def scan(n,keys=('ERROR','429','fail','expired','OOM','disk','DNS','pool','lag')):
  b='/task/fixtures/round-%02d/'%n
  for r,d,f in os.walk(b):
    for x in sorted(f):
      p=os.path.join(r,x);L=open(p).read().splitlines();print('##',p[len(b):],len(L))
      for i,l in enumerate(L,1):
        if x.endswith('.md') and l.strip() or any(k.lower() in l.lower() for k in keys):print(i,l[:150])
