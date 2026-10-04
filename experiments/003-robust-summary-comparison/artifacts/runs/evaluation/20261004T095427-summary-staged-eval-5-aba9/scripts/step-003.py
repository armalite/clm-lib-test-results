open('/task/workspace/notes.md','w').write('S1: rel-notes 7.20.4-0a00 line8 rates timeout 2500->600; line16 db pool 48->12. quotes-api.log first timeout line139 (600ms). deploys.log:4 deploy 08:16.\n')
import re
L=open('/task/fixtures/stage-1/logs/quotes-api.log').readlines()
for i,l in enumerate(L,1):
  if 'pool' in l or ('rates-svc' in l and 'timed out' not in l):print(i,l.strip()[:160])
  if i>400:break
I=open('/task/fixtures/stage-1/logs/ingress-a.log').readlines()
import collections;print(collections.Counter(re.search(r'status=(\d+)',l).group(1) for l in I))
print([i for i,l in enumerate(I,1) if 'status=5' in l][:5])