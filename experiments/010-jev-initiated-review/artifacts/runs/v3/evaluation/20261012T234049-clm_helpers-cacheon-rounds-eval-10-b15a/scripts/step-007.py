import re,glob
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=f.split('/')[-1]; hits=[]
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|WARN|FATAL|error|fail',l) and 'slow' not in l: hits.append((i,l.strip()[:150]))
  print(n,len(hits))
  for h in hits[:3]: print(' ',h)
  if hits: print('  lines',hits[0][0],'-',hits[-1][0])