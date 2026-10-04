import re
b='/task/fixtures/'
n=0
for i,l in enumerate(open(b+'logs/shipping-api.log'),1):
  if re.search(r'WARN|ERROR',l) and n<6: print(i,l.rstrip()[:180]); n+=1
for i,l in enumerate(open(b+'metrics/shipping-api.csv'),1):
  if 58<=i<=66: print(i,l.rstrip())