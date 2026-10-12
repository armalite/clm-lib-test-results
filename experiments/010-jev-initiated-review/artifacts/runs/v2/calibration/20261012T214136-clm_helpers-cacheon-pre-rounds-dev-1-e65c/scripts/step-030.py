import re
r='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(r+f),1):print(f,i,l.rstrip())
import os
for s in os.listdir(r+'logs'):
  ls=[(i,l) for i,l in enumerate(open(r+'logs/'+s),1) if re.search('ERROR|429|exhaust|fail|denied|invalid|OOM',l,re.I)]
  print(s,len(ls),[i for i,_ in ls][:15])
  for i,l in ls[:2]:print(' ',i,l.rstrip()[:200])