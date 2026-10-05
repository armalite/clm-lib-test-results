import re,glob
print(open('/task/fixtures/round-04/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    c={}
    for i,l in enumerate(open(f),1):
        if re.search(r'WARN|ERROR|FATAL|level=(warn|error)',l,re.I) and 'slow query' not in l:
            k=re.sub(r'\d+','#',l.strip())[:90]
            c.setdefault(k,[]).append(i)
    print(f.split('/')[-1])
    for k,v in c.items(): print(' ',len(v),v[:6],k)