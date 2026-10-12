import glob,collections
for f in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
    L=open(f).read().splitlines()
    bad=[(i+1,l) for i,l in enumerate(L) if any(k in l.lower() for k in ('error','warn','fail','429','pool','expired'))]
    print(f.split('/')[-1],len(L),len(bad))
    for i,l in bad[:3]:print(' ',i,l[:160])