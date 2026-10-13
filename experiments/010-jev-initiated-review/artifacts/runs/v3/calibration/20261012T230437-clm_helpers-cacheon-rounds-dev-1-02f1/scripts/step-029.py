import os,re
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  n=0
  for i,l in enumerate(open(b+'logs/'+f),1):
    if 'INFO' not in l:
      n+=1
      if n<=3:print(f,i,l.rstrip()[:160])
  print(f,'nonINFO',n)