import os,re
b='/task/fixtures/round-03/'
print(open(b+'board.md').read())
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if re.search(r'WARN|ERROR|FATAL',l) and 'slow query' not in l: print(f,i,l.strip()[:150])