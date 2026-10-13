import re,glob
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
 print('==',f);print(open(b+f).read())
for f in sorted(glob.glob(b+'logs/*.log')):
 L=[(i+1,l.strip()) for i,l in enumerate(open(f)) if not re.search('slow.query|INFO',l)]
 print('==',f.split('/')[-1],len(L))
 kinds={}
 for i,l in L:
  k=re.sub(r'[0-9]+','N',l)[-70:]
  kinds.setdefault(k,[]).append(i)
 for k,v in kinds.items(): print(v[0],v[-1],len(v),k)