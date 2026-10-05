import re,os
b='/task/fixtures/round-12/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f).read().splitlines(),1):print(f,i,l)
for f in sorted(os.listdir(b+'logs')):
  L=open(b+'logs/'+f).read().splitlines();d={}
  for i,l in enumerate(L,1):
    if '"ERROR"' in l or ' ERROR ' in l:
      k=re.sub(r'\d','#',l[60:110]);d.setdefault(k,[]).append(i)
  for k,v in d.items():print(f,k,v[0],v[-1],len(v))