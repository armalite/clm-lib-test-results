b='/task/fixtures/stage-3/logs/quotes-api.log'
n=0
for i,l in enumerate(open(b),1):
  if '22/22' in l:
    n+=1
    if n<3:print(i,l[:110].rstrip())
print(n)