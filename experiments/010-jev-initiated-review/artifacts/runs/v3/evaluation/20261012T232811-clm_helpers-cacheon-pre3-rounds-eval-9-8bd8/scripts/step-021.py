import os
r='/task/fixtures/round-05/'
print(os.listdir(r))
if os.path.exists(r+'changes.md'):print(open(r+'changes.md').read())
for f in ['shipping-svc','notify-worker']:
  L=[i for i,l in enumerate(open(r+'logs/'+f+'.log'),1) if ('tls' in l or 'disk' in l or 'pool' in l)]
  print(f,L[:20])
  ls=open(r+'logs/'+f+'.log').read().splitlines()
  print(ls[L[0]-1] if L else '')