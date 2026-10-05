import glob,re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f),1):print(f,i,l.rstrip())
for p in sorted(glob.glob('/task/fixtures/round-07/logs/*')):
  n=0
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|error|SERVFAIL|429|cert|heap|OOM|lag|disk',l,re.I) and n<4:
      n+=1;print(p.split('/')[-1],i,l.rstrip()[:160])