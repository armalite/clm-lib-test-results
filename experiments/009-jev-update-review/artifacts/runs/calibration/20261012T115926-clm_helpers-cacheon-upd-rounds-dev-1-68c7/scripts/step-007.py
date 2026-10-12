import glob
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    L=open(f).read().splitlines()
    print(f.split('/')[-1],len(L))
    for i,l in enumerate(L[:3],1): print(' ',i,l[:160])
import collections
for f in sorted(glob.glob('/task/fixtures/round-02/logs/*.log')):
    c=collections.Counter()
    for l in open(f):
        for w in ('error','warn','fail','429','timeout','refused','inflight'):
            if w in l.lower(): c[w]+=1
    print(f.split('/')[-1],dict(c))