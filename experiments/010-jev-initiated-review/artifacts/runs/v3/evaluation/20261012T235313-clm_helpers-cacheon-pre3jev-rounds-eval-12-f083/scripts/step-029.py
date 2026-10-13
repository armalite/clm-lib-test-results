import re
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-07/'+f),1):print(f,i,l.rstrip()[:200])
import glob
for p in sorted(glob.glob('/task/fixtures/round-07/logs/*')):
  n=p.split('/')[-1];hits=[]
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|WARN|429|cert|x509|refused|OOM|disk|pool|lag|NXDOMAIN',l,re.I) and 'slow' not in l: hits.append((i,l.strip()[:110]))
  print(n,len(hits))
  for h in hits[:4]:print(' ',h)
  print(' lines',[h[0] for h in hits])