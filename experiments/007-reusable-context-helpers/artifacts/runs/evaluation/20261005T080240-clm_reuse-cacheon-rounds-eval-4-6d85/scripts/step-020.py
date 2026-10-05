import re,glob,json,collections,ctx
out=[]
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    c=collections.defaultdict(list)
    for i,l in enumerate(open(f)):
        if re.search(r'WARN|ERROR',l) and 'slow query' not in l:
            m=re.search(r'"msg":"([^"]*)"',l); c[m.group(1) if m else l[:60]].append(i+1)
    for k,v in c.items(): out.append(f"{f.split('/')[-1]} {k} {v[0]}-{v[-1]} n={len(v)}")
print('\n'.join(out))
n=ctx.load()['entries'][0]['body']
ctx.reset(n+'\nR7: board.md:3 Thread B cause revised UPSTREAM_RATE_LIMIT. '+'; '.join(out))