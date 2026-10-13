import re,glob
d='/task/fixtures/round-04/'
print(open(d+'board.md').read())
for f in sorted(glob.glob(d+'logs/*.log')):
  L=open(f).read().splitlines();h=[i+1 for i,l in enumerate(L) if re.search('ERROR|WARN|FATAL|fail',l) and 'slow' not in l]
  print(f.split('/')[-1],len(h),h[:3],h[-1:] if h else '')
  if h: print(' ',L[h[0]-1][:200])