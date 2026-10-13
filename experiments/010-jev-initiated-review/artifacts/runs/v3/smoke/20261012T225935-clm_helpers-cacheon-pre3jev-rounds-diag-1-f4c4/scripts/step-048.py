import re
print(open('/task/fixtures/round-11/board.md').read())
for i,l in enumerate(open('/task/fixtures/round-11/logs/shipping-svc.log'),1):
    if re.search(r'error|fail|config|restart|pool',l,re.I): print(i,l.strip()[:160])