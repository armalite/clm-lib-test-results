import re
b='/task/fixtures/round-08/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import glob
for f in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|memory|OOM|restart|rss|heap',l,re.I) and 'gc' not in l.lower():print(f.split('/')[-1],i,l.strip()[:110])