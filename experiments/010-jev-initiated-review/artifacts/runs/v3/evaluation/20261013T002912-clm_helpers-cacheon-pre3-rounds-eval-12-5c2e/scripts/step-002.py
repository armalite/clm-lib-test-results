import os,re
b='/task/fixtures/round-01/logs/'
for f in sorted(os.listdir(b)):
  L=open(b+f).read().splitlines()
  print('==',f,L[0][:160])
  for i,l in enumerate(L,1):
    if re.search(r'ERROR|WARN|error|fail|429|ttl|pool|cert|dns',l,re.I):print(i,l[:150])