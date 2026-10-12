import glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
    L=open(f).read().splitlines()
    print(f.split('/')[-1],len(L),L[0][:150])
    for i,l in enumerate(L,1):
        if any(k in l.lower() for k in ['err','429','mem','heap','rss','oom','restart','fail','stamp','miss']): print(' ',i,l[:140])