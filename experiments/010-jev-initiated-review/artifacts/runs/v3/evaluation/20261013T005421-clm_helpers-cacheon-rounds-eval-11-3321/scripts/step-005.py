import os,re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+s),1):
    if 'slow query' in l or 'INFO' in l or 'info' in l.lower()[:60] and 'level=info' in l.lower():continue
    print(s,i,l.rstrip()[:160])