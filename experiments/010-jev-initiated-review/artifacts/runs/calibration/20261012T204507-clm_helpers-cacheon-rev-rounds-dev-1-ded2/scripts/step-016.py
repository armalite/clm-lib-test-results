import glob,re
b='/task/fixtures/round-05/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  n=f.split('/')[-1];hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|error|warn',l):hits.append((i,l.rstrip()[:150]))
  print(n,len(hits))
  for h in hits[:4]:print(' ',h)
  print('  lines',[h[0] for h in hits][:20])