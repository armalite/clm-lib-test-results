import subprocess
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
import glob
for p in sorted(glob.glob('/task/fixtures/round-08/logs/*')):
  L=[(i,l.rstrip()) for i,l in enumerate(open(p),1) if any(k in l for k in ('ERROR','429','SERVFAIL','backoff','retry','FATAL'))]
  print(p.split('/')[-1],len(L),L[:2],L[-1:] if L else '')