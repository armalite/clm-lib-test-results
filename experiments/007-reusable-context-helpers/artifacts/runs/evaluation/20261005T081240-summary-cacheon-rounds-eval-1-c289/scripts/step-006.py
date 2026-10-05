import glob,re
r='/task/fixtures/round-02/'
print(open(r+'board.md').read());print(open(r+'changes.md').read())
for f in sorted(glob.glob(r+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if 'INFO' not in l and 'slow query' not in l: print(f.split('/')[-1],i,l.rstrip()[:130])