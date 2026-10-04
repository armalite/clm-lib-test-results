import re
for f in ['logs/edge-gw.log','logs/payments-api.log']:
  n=0
  for i,l in enumerate(open('/task/fixtures/'+f),1):
    if re.search(r'expire|certif|x509|tls',l,re.I) and n<6: print(f,i,l.rstrip()[:200]); n+=1