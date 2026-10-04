L=open('/task/fixtures/stage-3/logs/payments-api.log').read().splitlines()
for i,l in enumerate(L,1):
  if '20/20' in l:print(i,l[:160]);break