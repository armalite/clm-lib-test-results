b='/task/fixtures/'
n=0
for i,l in enumerate(open(b+'logs/payments-api.log'),1):
  if 'ERROR' in l and n<5:print(i,l.rstrip()[:180]);n+=1
n=0
for i,l in enumerate(open(b+'logs/front-proxy.log'),1):
  if ('503' in l or 'ERROR' in l) and n<3:print(i,l.rstrip()[:180]);n+=1
L=open(b+'metrics/pricing-core-latency.csv').readlines()
for i in [0,1,60,100,128]:print(i+1,L[i].rstrip())