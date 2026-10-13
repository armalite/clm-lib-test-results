import re,glob
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip()[:200])
for p in sorted(glob.glob(b+'logs/*.log')):
  n=p.split('/')[-1];ids=[];s={}
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|FATAL|CRIT',l):
      ids.append(i);k=re.sub(r'\d','',l)[40:120];s.setdefault(k,(i,l.strip()[:170]))
  print(n,len(ids),ids[:25])
  for v in list(s.values())[:3]:print('  ',v)