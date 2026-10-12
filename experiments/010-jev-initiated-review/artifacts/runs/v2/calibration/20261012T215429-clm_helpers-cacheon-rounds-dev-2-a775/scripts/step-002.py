import re,collections
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read())
import glob
for p in sorted(glob.glob(b+'logs/*')):
  L=open(p).read().splitlines()
  print(p.split('/')[-1],L[0][:200])
  for i,l in enumerate(L,1):
    if re.search('ERROR|WARN|error|warn',l):print(i,l[:160])