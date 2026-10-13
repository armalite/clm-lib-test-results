import re,glob
b='/task/fixtures/round-05/'
print(open(b+'board.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|error|fail|429|pool|disk|mem|lag|cert|max_inflight',l,re.I):
      print(f.split('/')[-1],i,l.strip()[:150])