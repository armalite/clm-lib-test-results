b='/task/fixtures/stage-1/'
L=open(b+'logs/payments-api.log').readlines()
for i in (179,180,181):print(i,L[i-1].rstrip()[:170])
import re
n=0
for i,l in enumerate(L,1):
  if ('pool' in l or 'latency' in l or 'p99' in l) and n<5:print(i,l.rstrip()[:160]);n+=1
I=open(b+'logs/ingress-a.log').readlines()
n=0
for i,l in enumerate(I,1):
  if (' 5' in l and ('502' in l or '503' in l or '504' in l)) and n<3:print('ing',i,l.rstrip()[:160]);n+=1
print(len([l for l in I if ' 50' in l]))