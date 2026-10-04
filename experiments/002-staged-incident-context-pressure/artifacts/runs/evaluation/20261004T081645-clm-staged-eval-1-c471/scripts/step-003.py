import re
b='/task/fixtures/stage-1/logs/quotes-api.log'
n=0
for i,l in enumerate(open(b),1):
 if re.search(r'pool|exhaust|risk-score latency|p99',l,re.I):
  n+=1
  if n<6:print(i,l.rstrip()[:150])
print(n)