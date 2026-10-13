import os,re,collections
d='/task/fixtures/round-01/logs/'
for f in sorted(os.listdir(d)):
  L=open(d+f).read().splitlines()
  c=collections.Counter()
  ex={}
  for i,l in enumerate(L,1):
    if re.search(r'WARN|ERROR|error|fail|429|timeout',l,re.I):
      k=re.sub(r'\d+','N',l)[20:90];c[k]+=1;ex.setdefault(k,(i,l[:160]))
  print(f,len(L))
  for k,n in c.most_common(4):print(' ',n,ex[k])