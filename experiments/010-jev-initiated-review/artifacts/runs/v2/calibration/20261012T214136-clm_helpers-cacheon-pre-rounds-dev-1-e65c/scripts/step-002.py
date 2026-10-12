import glob,re
for p in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if re.search(r'WARN|ERROR|FATAL|error|fail',l):print(p.split('/')[-1],i,l.strip()[:160])