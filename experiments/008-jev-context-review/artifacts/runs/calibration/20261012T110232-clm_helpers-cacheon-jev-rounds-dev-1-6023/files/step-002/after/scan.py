import os,sys
b='/task/fixtures/round-%s'%sys.argv[1]
for r,d,f in os.walk(b):
  for x in sorted(f):
    p=os.path.join(r,x);print('==',p[len(b)+1:])
    for i,l in enumerate(open(p).read().splitlines(),1):
      if p.endswith('.md'):
        if l.strip(): print(i,l[:200])
      elif 'slow query' not in l and any(k in l.lower() for k in ('error','warn','fatal','crit')): print(i,l[:170])
