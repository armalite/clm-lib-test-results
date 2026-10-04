L=open('/task/fixtures/stage-1/logs/billing-svc.log').readlines()
n=0
for i,l in enumerate(L,1):
  if 'timed out' in l:
    n+=1
    if n in(1,95):print(i,l.rstrip()[:200])
P=open('/task/fixtures/stage-1/logs/front-proxy.log').readlines()
for i,l in enumerate(P,1):
  if ' 50' in l:print(i,l.rstrip()[:200]);break