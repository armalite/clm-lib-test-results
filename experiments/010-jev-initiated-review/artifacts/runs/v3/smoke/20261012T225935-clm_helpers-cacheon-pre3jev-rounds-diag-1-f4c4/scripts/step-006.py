t=open('/task/workspace/spill/s5.obs.txt').read()
import re
for l in t.splitlines():
  if l.startswith(('board','changes')):print(l[:160])
ls=[l for l in t.splitlines() if not l.startswith(('board','changes'))]
print(len(ls))
for l in ls[:30]:print(l[:120])