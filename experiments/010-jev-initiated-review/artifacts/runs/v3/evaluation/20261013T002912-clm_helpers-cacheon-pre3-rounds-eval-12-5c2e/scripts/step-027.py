import os,re
b='/task/fixtures/round-07/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  n=0
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search('ERROR|WARN|429|expired|fail',l) and 'slow' not in l:
      n+=1
      if n<=4:print(f,i,l.rstrip()[:170])
  print(f,'n=',n)