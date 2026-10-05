import re,glob
b='/task/fixtures/round-02/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for f in sorted(glob.glob(b+'logs/*.log')):
  seen=set()
  for i,l in enumerate(open(f),1):
    if re.search(r'WARN|ERROR|fail|429|timeout|FATAL',l,re.I):
      k=re.sub(r'\d+','#',l)[20:110]
      if k in seen: continue
      seen.add(k);print(f.split('/')[-1],i,l.strip()[:200])