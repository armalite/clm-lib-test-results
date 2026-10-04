L=open('/task/fixtures/metrics/pricing-core-latency.csv').readlines()
for i in [0,1,60,100,128]:print(i+1,L[i].rstrip())
import re
for f in ['logs/payments-api.log','logs/front-proxy.log']:
  n=0
  for i,l in enumerate(open('/task/fixtures/'+f),1):
    if re.search('timeout|timed out|ERROR',l,re.I):
      n+=1
      if n<4:print(f,i,l.rstrip()[:200])
  print(f,n)