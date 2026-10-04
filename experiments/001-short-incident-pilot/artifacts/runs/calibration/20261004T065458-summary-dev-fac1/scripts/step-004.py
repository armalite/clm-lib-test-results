import re
b='/task/fixtures/'
n=0
for i,l in enumerate(open(b+'logs/shipping-api.log'),1):
  if l[11:16]>='08:28' and re.search(r'ERROR|pool',l) and n<6: print(i,l.rstrip()[:200]); n+=1