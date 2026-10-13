import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  hits=[(i,l.strip()[:150]) for i,l in enumerate(open(f),1) if re.search(r'ERROR|WARN|429|certificate|error',l) and 'slow' not in l]
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]: print(h)