import glob,re
r='/task/fixtures/round-02/'
print(open(r+'board.md').read())
for f in sorted(glob.glob(r+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|429|pool|expired|DNS|lag|OOM|disk',l,re.I) and 'slow query' not in l:
      print(f.split('/')[-1],i,l.strip()[:150])