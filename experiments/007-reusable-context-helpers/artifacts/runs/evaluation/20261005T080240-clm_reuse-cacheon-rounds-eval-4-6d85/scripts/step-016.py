import os,re,collections
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines()
  c=collections.Counter();first={};last={}
  for i,l in enumerate(L,1):
    if re.search('WARN|ERROR|FATAL',l,re.I):
      k=re.sub(r'[0-9]+','#',l)[30:110];c[k]+=1;first.setdefault(k,i);last[k]=i
  print(f,len(L))
  for k,v in c.most_common(4):print(' ',v,first[k],last[k],k)
  print('  sample:',L[0][:160])