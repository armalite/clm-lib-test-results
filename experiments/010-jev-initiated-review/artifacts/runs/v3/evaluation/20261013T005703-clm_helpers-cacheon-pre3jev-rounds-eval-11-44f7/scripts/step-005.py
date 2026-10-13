import os,glob
b='/task/fixtures/round-02/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(f),1):
    if 'ERROR' in l or 'FATAL' in l: print(os.path.basename(f),i,l.strip()[:160])