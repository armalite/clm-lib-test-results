import re
for f in ['logs/edge-gw.log','logs/payments-api.log']:
  print('==',f);n=0
  for i,l in enumerate(open('/task/fixtures/'+f),1):
    if re.search('cert|expir|tls|x509',l,re.I) and n<8:n+=1;print(i,l.rstrip()[:200])
print(open('/task/fixtures/deploy/changes.log').read().splitlines()[12])