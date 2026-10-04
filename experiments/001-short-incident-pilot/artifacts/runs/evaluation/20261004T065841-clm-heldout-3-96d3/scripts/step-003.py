import re
b='/task/fixtures/logs/'
for f in ['inventory-svc.log','front-proxy.log']:
  n=0
  for i,l in enumerate(open(b+f),1):
    if re.search(r'ERROR|encoder| 50[0-9] ',l) and n<6:
      print(f,i,l.rstrip()[:170]);n+=1