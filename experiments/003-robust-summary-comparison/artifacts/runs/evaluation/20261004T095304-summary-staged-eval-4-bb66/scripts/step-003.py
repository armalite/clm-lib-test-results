b='/task/fixtures/stage-1/logs/payments-api.log'
for i,l in enumerate(open(b),1):
  if 'db pool' in l or 'tax-engine' in l or 'pool' in l.lower() and 'ERROR' in l:print(i,l.rstrip()[:170])