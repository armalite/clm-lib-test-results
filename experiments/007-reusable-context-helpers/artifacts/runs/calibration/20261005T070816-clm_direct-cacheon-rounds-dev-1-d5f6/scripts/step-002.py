import os,re,collections
d='/task/fixtures/round-01/logs/'
for f in sorted(os.listdir(d)):
  L=open(d+f).read().splitlines()
  print('==',f,L[0][:160])
  c=collections.Counter()
  for i,l in enumerate(L,1):
    if re.search(r'WARN|ERROR|error|fail|429|timeout',l,re.I):
      k=re.sub(r'\d+','N',l[20:])[:90];c[k]+=1
      if c[k]==1:print(i,l[:170])
