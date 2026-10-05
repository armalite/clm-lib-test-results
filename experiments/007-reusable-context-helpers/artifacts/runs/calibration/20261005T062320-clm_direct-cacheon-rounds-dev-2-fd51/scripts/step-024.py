import re,glob
print(open('/task/fixtures/round-08/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    n=0
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|error|429|SERVFAIL|cert|invalid|FATAL',l) and 'slow query' not in l:
            n+=1
            if n<=3: print(f.split('/')[-1],i,l.strip()[:160])
    print(f.split('/')[-1],'count',n)