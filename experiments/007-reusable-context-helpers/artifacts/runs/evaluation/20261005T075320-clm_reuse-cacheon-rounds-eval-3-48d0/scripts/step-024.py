import ctx
ctx.keep_only(['n1','n2','n3','n4','n4b','n5','n6','n7'])
t=open('spill/s23.obs.txt').read()
for l in t.splitlines():
  if 'board' in l or 'changes' in l: print(l[:160])
import collections
c=collections.defaultdict(list)
for l in t.splitlines():
  p=l.split(' ',2)
  if len(p)>2 and p[0].endswith('.log'):
    k=(p[0],'429' if '429' in p[2] else 'heap' if 'heap' in p[2].lower() else 'disk' if 'disk' in p[2].lower() else 'cfg' if 'config' in p[2].lower() else 'cert' if 'cert' in p[2].lower() else 'oth')
    c[k].append(p[1])
for k,v in c.items():print(k,','.join(v))