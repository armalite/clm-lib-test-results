open('/task/workspace/notes.txt','w').write('S1: ledger timeout 600 set by release-notes-8.15.4-7744.md:11; deploy deploys.log:5; symptom profile-svc.log:131 timeout 600ms. db pool 14 (rn:17) also.\n')
import re
L=open('/task/fixtures/stage-1/logs/profile-svc.log').read().splitlines()
for i,l in enumerate(L,1):
 if 'db pool' in l: print(i,l[:200])
G=open('/task/fixtures/stage-1/logs/api-gateway.log').read().splitlines()
for i,l in enumerate(G,1):
 if '503' in l: print(i,l[:200]);break