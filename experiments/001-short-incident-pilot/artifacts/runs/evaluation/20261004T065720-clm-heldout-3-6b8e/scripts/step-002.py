import re
for f in ['logs/inventory-svc.log','logs/front-proxy.log']:
 n=0
 for i,l in enumerate(open('/task/fixtures/'+f),1):
  if re.search(r'ERROR|FATAL|flag|ff-|50[03]',l) and n<8:print(f,i,l.rstrip()[:180]);n+=1