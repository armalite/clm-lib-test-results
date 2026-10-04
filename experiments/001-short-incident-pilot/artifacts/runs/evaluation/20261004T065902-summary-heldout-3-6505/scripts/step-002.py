import re
b='/task/fixtures/logs/'
for f in ['inventory-svc.log','front-proxy.log']:
  L=open(b+f).read().splitlines();n=0
  for i,l in enumerate(L,1):
    if re.search(r'ERROR|FATAL|flag|ff-|panic|exception',l,re.I) and n<12:print(f,i,l[:200]);n+=1