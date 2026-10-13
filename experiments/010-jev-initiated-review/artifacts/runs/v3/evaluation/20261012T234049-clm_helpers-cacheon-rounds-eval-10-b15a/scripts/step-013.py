import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
import glob
for f in sorted(glob.glob(b+'logs/*')):
  L=open(f).read().splitlines();h=[i+1 for i,l in enumerate(L) if re.search('ERROR|WARN|FATAL|fail',l) and 'slow' not in l]
  print(f.split('/')[-1],len(h),h[:3],h[-1:] if h else '', L[h[0]-1][:160] if h else '')