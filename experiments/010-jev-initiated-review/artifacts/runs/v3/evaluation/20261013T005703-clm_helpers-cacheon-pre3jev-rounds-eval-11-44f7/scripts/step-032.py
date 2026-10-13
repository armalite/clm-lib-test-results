import os,re
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  n=0
  for i,l in enumerate(open(b+'logs/'+s),1):
    if re.search('ERROR|WARN|level=(error|warn)',l,re.I):
      n+=1
      if n<=4:print(s,i,l.rstrip()[:160])
  print(s,'count',n)