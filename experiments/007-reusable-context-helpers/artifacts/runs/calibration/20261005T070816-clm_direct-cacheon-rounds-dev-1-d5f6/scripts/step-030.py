import re,glob
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
  seen=set()
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|fail|429|exhaust|max_inflight',l):
      k=re.sub(r'\d','',l)[-60:]
      if k in seen:continue
      seen.add(k);print(f.split('/')[-1],i,l.rstrip()[:150])