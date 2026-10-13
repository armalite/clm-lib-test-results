import os,re
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+s),1):
    if 'slow query' in l: continue
    if re.search(r'INFO|DEBUG',l) and not re.search(r'error|fail|429|expire|pool|lag|mem|disk|dns|cert',l,re.I): continue
    print(s,i,l.rstrip()[:160])