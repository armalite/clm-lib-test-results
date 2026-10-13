import json,re,glob,os
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='notes']
json.dump(d,open('/task/workspace/context.json','w'))
R='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(R+f),1): print(f,i,l.rstrip())
for f in sorted(glob.glob(R+'logs/*.log')):
  h=[(i,l) for i,l in enumerate(open(f),1) if re.search(r'ERROR|FATAL|CRIT',l,re.I)]
  msgs=set(re.sub(r'.*"msg":"([^"]*)".*',r'\1',l.strip())[:80] for i,l in h)
  print(os.path.basename(f),len(h),h[0][0] if h else '',h[-1][0] if h else '',list(msgs)[:3])
  if h: print(h[0][1][:200])