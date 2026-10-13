import glob,re
print(open('/task/fixtures/round-09/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  L=open(f).read().splitlines()
  er=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|error|FATAL',l)]
  print(f.split('/')[-1],len(er),er[:1],er[-1:] if er else '')