p='/task/fixtures/stage-3/'
for i,l in enumerate(open(p+'logs/payments-api.log'),1):
  if '18/18' in l: print(i,l.strip()[:150]);break
for i,l in enumerate(open(p+'logs/ingress-a.log'),1):
  if ' 503' in l or '=503' in l:
    if l[11:16]>'10:48': print(i,l.strip()[:150]);break