import re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/**/*',recursive=True)):
  if f.endswith('.md'):
    print(f, open(f).read())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|FATAL|error|fail|expired|invalid|429|oom',l) and 'slow query' not in l:
      print(f.split('/')[-1],i,l.strip()[:150])
