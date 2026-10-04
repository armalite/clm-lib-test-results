n=0
for i,l in enumerate(open('/task/fixtures/stage-3/logs/returns-svc.log'),1):
  if '16/16' in l:
    n+=1
    if n<3:print(i,l.rstrip())
print(n)