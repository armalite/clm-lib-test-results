t=open('/task/workspace/spill/s5.obs.txt').read().splitlines()
for l in t:
  if l.startswith('shipping') and 'slow query' not in l:print(l[:130])