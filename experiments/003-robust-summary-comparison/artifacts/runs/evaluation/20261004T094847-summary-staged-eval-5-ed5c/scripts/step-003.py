open('/task/workspace/notes.txt','w').write('S1: rates-svc timeout 2500->600 in release-notes-7.20.4-0a00.md:8; db pool 48->12 line16; errors quotes-api.log:139 timed out 600ms; ingress-a.log:71 503\n')
import re
L=open('/task/fixtures/stage-1/logs/quotes-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if ('pool' in l or 'rates-svc' in l and 'ERROR' not in l):print(i,l[:180])
