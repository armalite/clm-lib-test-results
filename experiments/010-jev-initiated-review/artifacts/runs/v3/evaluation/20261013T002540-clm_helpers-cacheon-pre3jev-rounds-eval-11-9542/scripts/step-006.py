import os
b='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for s in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+s),1):
    if 'WARN slow query' in l: continue
    if any(k in l for k in ['ERROR','error','FATAL','429','pool','cert','DNS','lag','memory','disk','batch']): print(s,i,l.rstrip()[:160])