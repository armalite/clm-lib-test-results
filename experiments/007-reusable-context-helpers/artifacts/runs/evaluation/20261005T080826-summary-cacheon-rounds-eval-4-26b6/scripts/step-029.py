import os,re
b='/task/fixtures/round-10/'
for i,l in enumerate(open(b+'board.md'),1):print('board',i,l.rstrip())
for i,l in enumerate(open(b+'changes.md'),1):print('chg',i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  L=[i for i,l in enumerate(open(b+'logs/'+f),1) if 'ERROR' in l]
  m=set(re.sub(r'\d+','N',l)[60:150] for i,l in enumerate(open(b+'logs/'+f),1) if 'ERROR' in l)
  print(f,L[:12],len(L),list(m)[:2])
open('/task/workspace/notes.md','a').write('\nR10 read step29\n')