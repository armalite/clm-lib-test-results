import re
open('/task/workspace/notes.md','w').write('S1: release-notes-6.24.0-4314.md:9 timeout 2500->800; :18 pool 48->10. billing log ERROR pricing-core timed out after 800ms lines 152-220 (95 errors). deploys.log:5.\n')
L=open('/task/fixtures/stage-1/logs/billing-svc.log').read().splitlines()
n=0
for i,l in enumerate(L,1):
  if re.search(r'pool|pricing-core.*ok|latency',l,re.I):
    n+=1
    if n<6:print(i,l[:180])
print(n)