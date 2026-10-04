import re
for f in ['logs/edge-gw.log','logs/payments-api.log']:
  print('==',f)
  n=0
  for i,l in enumerate(open('/task/fixtures/'+f),1):
    if re.search(r'(?i)cert|expir|tls|x509',l) and n<8: print(i,l.rstrip()[:180]); n+=1
print(open('/task/fixtures/deploy/changes.log').readlines()[12][150:])