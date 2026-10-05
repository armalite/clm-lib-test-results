import re,glob
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  seen=set()
  for i,l in enumerate(open(f),1):
    if re.search(r'WARN|ERROR|fail|429|timeout|exhaust|cert|dns|OOM|disk|lag',l,re.I):
      k=re.sub(r'\d+','N',l)[:90]
      if k in seen: continue
      seen.add(k);print(f.split('/')[-1],i,l.strip()[:160])