import glob
r='/task/fixtures/round-04/'
print(open(r+'board.md').read())
for f in sorted(glob.glob(r+'logs/*.log')):
    L=open(f).read().splitlines()
    e=[(i+1,l) for i,l in enumerate(L) if 'ERROR' in l or 'error' in l.lower()]
    print(f.split('/')[-1],len(e))
    for i,l in e[:3]: print(i,l[:160])
