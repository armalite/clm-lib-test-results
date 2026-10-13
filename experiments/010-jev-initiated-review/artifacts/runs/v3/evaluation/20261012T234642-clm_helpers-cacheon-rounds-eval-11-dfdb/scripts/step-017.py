import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-06/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*')):
  n=f.split('/')[-1];hits=[]
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|FATAL|429|dns|cert|pool|OOM|disk|lag|batch',l,re.I) and 'slow' not in l:hits.append((i,l.strip()[:110]))
  print(n,len(hits))
  for h in hits[:5]:print(' ',h)
  print('  lines',[h[0] for h in hits])