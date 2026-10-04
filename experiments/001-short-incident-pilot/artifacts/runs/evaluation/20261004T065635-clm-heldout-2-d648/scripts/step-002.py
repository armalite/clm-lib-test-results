import os,re
os.chdir('/task/fixtures')
n=0
for i,l in enumerate(open('logs/payments-api.log'),1):
  if re.search('ERROR',l) and n<4: print(i,l.rstrip()[:200]);n+=1
L=open('metrics/pricing-core-latency.csv').readlines();print(L[0],L[60],L[100])