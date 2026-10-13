import glob,re
print(open('/task/fixtures/round-07/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[(i+1,l) for i,l in enumerate(L) if re.search(r'ERROR|error|FATAL|429|SERVFAIL|OOM|disk',l)]
    print(f.split('/')[-1],len(hits))
    for i,l in hits[:5]: print(' ',i,l[:160])