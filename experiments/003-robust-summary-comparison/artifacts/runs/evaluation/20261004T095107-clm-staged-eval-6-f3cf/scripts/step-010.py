n=0
for i,l in enumerate(open('/task/fixtures/stage-3/logs/billing-svc.log'),1):
  if '16/16' in l:
    n+=1
    if n<4:print(i,l.rstrip()[:120])
print(n)