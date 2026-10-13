for f in ['board.md','changes.md']:
    for i,l in enumerate(open('/task/fixtures/round-11/'+f),1):print(f,i,l.rstrip())
for i,l in enumerate(open('/task/fixtures/round-11/logs/shipping-svc.log'),1):
    if i<6 or 'ERROR' in l or 'config' in l.lower():print(i,l.rstrip()[:160])
