import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-03/'+f),1): print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-03/logs/*.log')):
  ls=[(i,l.strip()) for i,l in enumerate(open(p),1) if re.search(r'ERROR|WARN|error|fail',l)]
  if ls: print(p.split('/')[-1],len(ls),ls[0][0],ls[-1][0],ls[0][1][:150])