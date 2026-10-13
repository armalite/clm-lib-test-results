import re,glob
p='/task/fixtures/round-03/'
print(open(p+'board.md').read())
for f in sorted(glob.glob(p+'logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|FATAL|SERVFAIL|429|inflight|OOM|disk|cert',l,re.I):
            print(f.split('/')[-1],i,l.strip()[:150])