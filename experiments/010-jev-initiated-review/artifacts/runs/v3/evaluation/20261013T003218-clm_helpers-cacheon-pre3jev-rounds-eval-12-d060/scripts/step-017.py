b='/task/fixtures/round-04/logs/'
for i,l in enumerate(open(b+'ledger-svc.log'),1):
  if 'ERR' in l or 'lag' in l: print(i,l.rstrip()[:160])