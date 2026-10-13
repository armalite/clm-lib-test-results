t=open('/task/workspace/spill/s6.obs.txt').read()
print(t[:2500])
print('...')
import re
for l in t.splitlines():
  if 'ERROR' in l and 'board' not in l: pass
print(len(t))