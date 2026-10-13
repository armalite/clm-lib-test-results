import glob
for f in ['board.md','changes.md']:
 print(f);print(open('/task/fixtures/round-02/'+f).read())
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*')):
 for i,l in enumerate(open(f),1):
  if 'slow query' in l and 'WARN' in l: continue
  if 'INFO' in l: continue
  print(f.split('/')[-1],i,l.strip()[:160])