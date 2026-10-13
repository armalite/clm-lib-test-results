import os
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+f),1):
    if any(k in l for k in ['ERROR','error','fail','429','expired','SERVFAIL','pool','inflight']) and 'slow query' not in l: print(f,i,l.rstrip()[:150])