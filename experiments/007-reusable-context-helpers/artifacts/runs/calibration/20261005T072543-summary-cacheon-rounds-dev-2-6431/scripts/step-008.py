import re
f='/task/fixtures/round-03/logs/auth-svc.log'
L=[i for i,l in enumerate(open(f),1) if 'certificate_expired' in l]
c=[i for i,l in enumerate(open('/task/fixtures/round-03/logs/checkout-api.log'),1) if 'SERVFAIL' in l]
v=[i for i,l in enumerate(open('/task/fixtures/round-03/logs/inventory-svc.log'),1) if 'SERVFAIL' in l]
s='R3: Thread B opened auth-svc DB_POOL_EXHAUSTED ongoing (round-03/board.md:3) BUT logs show CERT_EXPIRED peer=sso.example.net auth lines %s. DNS continues checkout %s inventory %s. CHG-126 PROPOSED only.\n'%(L,c,v)
open('/task/workspace/notes.md','a').write(s);print(s)