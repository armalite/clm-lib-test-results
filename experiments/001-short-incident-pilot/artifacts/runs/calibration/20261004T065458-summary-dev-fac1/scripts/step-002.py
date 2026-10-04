import re
b='/task/fixtures/'
for f in ['logs/shipping-api.log','logs/ingress-a.log']:
  n=0
  for i,l in enumerate(open(b+f),1):
    if re.search(r'pool|exhaust|ERROR|cert|expire',l,re.I) and n<8: print(f,i,l.rstrip()[:200]); n+=1
for i,l in enumerate(open(b+'metrics/shipping-api.csv'),1):
  if i<3 or i%20==0: print(i,l.rstrip())