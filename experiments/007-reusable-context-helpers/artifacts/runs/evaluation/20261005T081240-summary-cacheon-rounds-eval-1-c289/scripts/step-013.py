b='/task/fixtures/round-04/logs/shipping-svc.log'
L=[i for i,l in enumerate(open(b),1) if 'certificate_expired' in l]
print(L)
open('/task/workspace/notes.md','a').write('\nR4: board Thread B shipping-svc suspected DB_POOL_EXHAUSTED ongoing (round-04/board.md:3). Logs actually show CERT_EXPIRED sso.example.net in shipping-svc lines '+str(L)+'. Follow-up RUNBOOK_UPDATE OPEN (round-04/board.md:4). CHG-133 noise.\n')
