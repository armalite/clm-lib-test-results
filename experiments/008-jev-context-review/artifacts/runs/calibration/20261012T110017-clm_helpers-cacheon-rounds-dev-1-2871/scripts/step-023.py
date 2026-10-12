import sys;sys.path.insert(0,'/task/workspace')
import h
t=open('/task/workspace/spill/s22.obs.txt').read()
ls=t.splitlines()
print('\n'.join(ls[:12]))
print(len(ls))
for l in ls[12:]:
  if '429' not in l: print(l[:150])
import json
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body']
h.setctx([{'id':'n1','role':'note','body':n+' R7 board empty. R8 advanced; scanned in step 23 (see obs).'}])