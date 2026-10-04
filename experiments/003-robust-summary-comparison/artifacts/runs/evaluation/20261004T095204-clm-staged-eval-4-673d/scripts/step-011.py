L=open('/task/fixtures/stage-3/logs/payments-api.log').read().splitlines()
c=0
for i,l in enumerate(L,1):
  if '18/18' in l and c<3: print(i,l[:90]);c+=1
L=open('/task/fixtures/stage-1/deploy/release-notes-6.25.3-646f.md').read().splitlines()
for i,l in enumerate(L,1):
  if 'pool' in l: print(i,l)