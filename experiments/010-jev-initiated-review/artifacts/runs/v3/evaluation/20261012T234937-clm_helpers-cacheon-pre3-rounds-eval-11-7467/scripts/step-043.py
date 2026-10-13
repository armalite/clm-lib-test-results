import re,glob
print(open('/task/fixtures/round-11/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*')):
  L=[i+1 for i,l in enumerate(open(f)) if re.search('ERROR|error|SERVFAIL|429|fail',l)]
  print(f.split('/')[-1],len(L),L[:1],L[-1:])
  for i,l in enumerate(open(f)):
    if i+1 in L[:1]: print(l[:200])