import re,glob
b='/task/fixtures/round-10/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'429|pool|config validation|ERROR',l): print(f.split('/')[-1],i,l.strip()[:110])