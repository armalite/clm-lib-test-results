import re
b='/task/fixtures/logs/'
for f in ['inventory-svc.log','front-proxy.log']:
  n=0
  for i,l in enumerate(open(b+f),1):
    if re.search(r'ERROR|WARN|flag|ff-|Exception|panic',l) and n<15:
      print(f,i,l.rstrip()[:180]);n+=1