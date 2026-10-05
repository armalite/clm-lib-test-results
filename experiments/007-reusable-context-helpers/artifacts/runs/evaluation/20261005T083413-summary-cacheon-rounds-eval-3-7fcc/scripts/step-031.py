import os,glob
b='/task/fixtures/round-10/'
for i,l in enumerate(open(b+'board.md'),1):print('board',i,l.rstrip())
if os.path.exists(b+'changes.md'):
  for i,l in enumerate(open(b+'changes.md'),1):print('chg',i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if '"INFO"' in l or 'slow query' in l:continue
    print(os.path.basename(f),i,l.rstrip()[:150])