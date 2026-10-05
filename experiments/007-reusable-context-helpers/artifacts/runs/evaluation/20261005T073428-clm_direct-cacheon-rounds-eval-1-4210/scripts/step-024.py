import re,glob
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|lag|429|expired|pool|OOM|disk',l,re.I) and 'slow query' not in l:hits.append((i,l.rstrip()[:150]))
  print(f.split('/')[-1],len(hits),[h[0] for h in hits])
  for h in hits[:2]:print(' ',h)