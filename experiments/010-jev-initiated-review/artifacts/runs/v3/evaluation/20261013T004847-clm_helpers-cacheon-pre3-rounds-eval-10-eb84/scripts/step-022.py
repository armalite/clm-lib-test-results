import re,collections
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
import os
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  c=collections.Counter();first={}
  for i,l in enumerate(L,1):
    if re.search('ERROR|WARN|error|fail|429|SERVFAIL|pool|OOM|disk',l,re.I):
      k=re.sub(r'\d+','#',l)[30:110];c[k]+=1;first.setdefault(k,i)
  print(f,len(L))
  for k,n in c.most_common(4):print('  ',n,first[k],k)