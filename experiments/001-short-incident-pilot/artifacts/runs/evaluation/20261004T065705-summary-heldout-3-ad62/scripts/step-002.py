import re
b='/task/fixtures/logs/'
for f in ['inventory-svc.log','front-proxy.log']:
  n=0
  for i,l in enumerate(open(b+f),1):
    if re.search(r'ERROR|ff-|flag|panic|exception',l,re.I):
      n+=1
      if n<=12:print(f,i,l.rstrip()[:170])
  print(f,'count',n)