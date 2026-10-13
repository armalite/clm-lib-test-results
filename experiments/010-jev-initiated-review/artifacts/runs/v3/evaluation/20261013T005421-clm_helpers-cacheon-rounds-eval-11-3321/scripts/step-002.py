import glob,re
b='/task/fixtures/round-01/logs/'
for p in sorted(glob.glob(b+'*.log')):
  L=open(p).read().splitlines()
  print(p.split('/')[-1],L[0][:160])
  for i,l in enumerate(L,1):
    if re.search(r'ERROR|WARN|error|fail|429|timeout',l):print(i,l[:150])