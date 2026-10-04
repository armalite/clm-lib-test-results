b='/task/fixtures/stage-3/logs/billing-svc.log'
n=0
for i,l in enumerate(open(b),1):
  if '/16 ' in l:
    n+=1
    if n<3:print(i,l.rstrip())
print(n)