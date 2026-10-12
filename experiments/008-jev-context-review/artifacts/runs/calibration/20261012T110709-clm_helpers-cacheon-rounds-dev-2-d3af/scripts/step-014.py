import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-05/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(f),1) if re.search('ERROR|WARN|error|fail',l) and 'slow query' not in l]
  print(f.split('/')[-1],len(L))
  for x in L[:3]+L[-1:]:print(' ',x[0],x[1][:150])