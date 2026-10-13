import re,glob
b='/task/fixtures/round-02/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(f),1):
    if not re.search(r'slow.query|INFO',l,re.I): print(f.split('/')[-1],i,l.strip()[:160])