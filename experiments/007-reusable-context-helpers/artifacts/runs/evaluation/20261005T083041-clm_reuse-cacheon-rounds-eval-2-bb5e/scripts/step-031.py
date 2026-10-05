import re,glob
print(open('/task/fixtures/round-11/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*.log')):
  L=[i+1 for i,l in enumerate(open(f)) if re.search(r'SERVFAIL|certificate|validation failed|heap|restart|ERROR',l)]
  print(f.split('/')[-1],len(L),L[:1],L[-1:])
import ctx
d=ctx.load();d['entries']=[e for e in d['entries'] if e['id'].startswith('n')];ctx.save(d)