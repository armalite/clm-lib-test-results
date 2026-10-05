import re,glob,collections,ctx
out=[]
for fn in ['board.md','changes.md']:
    b=open('/task/fixtures/round-09/'+fn).read().splitlines()
    for i,l in enumerate(b):
        if l.strip(): out.append(f'{fn}:{i+1}:{l}')
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
    c=collections.defaultdict(list)
    for i,l in enumerate(open(f)):
        if re.search(r'WARN|ERROR|warn|error',l) and 'slow query' not in l:
            m=re.search(r'"msg":"([^"]*)"',l); c[m.group(1) if m else l[:70]].append(i+1)
    for k,v in c.items(): out.append(f"{f.split('/')[-1]} {k} {v[0]}-{v[-1]} n={len(v)}")
s='\n'.join(out);print(s)
n=ctx.load()['entries'][0]['body']
ctx.reset(n+'\nR9: '+s[:900])