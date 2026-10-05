import glob,re
b='/task/fixtures/round-03/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
  n=f.split('/')[-1];c=0
  for i,l in enumerate(open(f),1):
    if 'slow query' in l:continue
    if re.search(r'ERROR|WARN|error|fail|429|max_inflight',l,re.I):
      c+=1
      if c<=4:print(n,i,l.rstrip()[:150])
  print(n,'count',c)
  print(n,'L1',open(f).readline().rstrip()[:150])