import re
L=open('/task/fixtures/metrics/pricing-core-latency.csv').readlines()
for i in [0,1,2,60,100,128]:
  if i<len(L): print(i+1,L[i].rstrip())
for i,l in enumerate(open('/task/fixtures/logs/payments-api.log'),1):
  if re.search('timeout|ERROR',l,re.I):
    print(i,l.rstrip()[:200]); break
c=0
for i,l in enumerate(open('/task/fixtures/logs/payments-api.log'),1):
  if 'timeout' in l.lower(): c+=1
print('count',c)