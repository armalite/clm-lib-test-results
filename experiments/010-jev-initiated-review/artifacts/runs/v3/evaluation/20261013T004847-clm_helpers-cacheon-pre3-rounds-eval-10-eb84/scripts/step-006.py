import re
b='/task/fixtures/round-02/'
print(open(b+'board.md').read())
import glob
for f in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(f),1):
    if 'slow query' in l: continue
    if re.search('ERROR|WARN|FATAL|429|timeout|refused',l,re.I): print(f.split('/')[-1],i,l.strip()[:160])