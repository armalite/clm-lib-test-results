import json,re
s=open('/task/workspace/spill/s25.obs.txt').read()
out=[]
for l in s.splitlines():
  if 'logs' in l or '.log' in l: continue
  out.append(l)
print('\n'.join(out)[:1500])
cnt={}
for l in s.splitlines():
  m=re.match(r'(\S+\.log) (\d+) .*?(ERROR|FATAL|CRIT)\s+\S+\s+(.{0,45})',l)
  if m:
    k=(m.group(1),re.sub(r'\d+','#',m.group(4)));cnt.setdefault(k,[]).append(m.group(2))
for k,v in cnt.items(): print(k,','.join(v))
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id'] in('n1','n2','n3','n4')]+[{'id':'n5p','role':'note','body':'Round5 released; raw errors in /task/workspace/spill/s25.obs.txt (analysing).'}]
json.dump(ctx,open('/task/workspace/context.json','w'))