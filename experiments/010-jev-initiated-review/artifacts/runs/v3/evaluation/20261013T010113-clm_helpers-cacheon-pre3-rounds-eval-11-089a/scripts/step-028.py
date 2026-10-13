import re,glob,collections
c=collections.defaultdict(list)
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|CRIT|429|fail',l):
      k=(f.split('/')[-1],re.sub(r'\d+','#',l.split(' ',3)[-1])[:60].strip());c[k].append(i)
for k,v in c.items():print(k,v)
print(open('/task/fixtures/round-05/board.md').read())