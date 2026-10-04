L=open('/task/fixtures/stage-3/logs/returns-svc.log').readlines()
n=0
for i,l in enumerate(L,1):
 if '16/16' in l:
  n+=1
  if n<3:print(i,l.strip()[:150])
print(n)