import glob,re
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*')):
  n=f.split('/')[-1];hits=[]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|error|fail|expired|SERVFAIL|disk|pool|429|config',l,re.I): hits.append(i)
  print(n,len(hits),hits[:25])
  if hits: print(open(f).read().splitlines()[hits[0]-1][:200])