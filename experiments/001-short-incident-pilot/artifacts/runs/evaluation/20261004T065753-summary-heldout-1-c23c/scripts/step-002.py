import re
for f in ['logs/edge-gw.log','logs/payments-api.log']:
    print('==',f)
    for i,l in enumerate(open('/task/fixtures/'+f),1):
        if re.search(r'expir|cert|tls|x509',l,re.I): print(i,l.rstrip()[:200])
