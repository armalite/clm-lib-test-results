p='/task/fixtures/stage-3/'
for i,l in enumerate(open(p+'deploy/changes.log'),1):print(i,l.rstrip())
L=open(p+'logs/billing-svc.log').read().splitlines()
h=[i+1 for i,l in enumerate(L) if 'pool' in l]
print(len(h),h[:5]);print(L[h[0]-1][:200] if h else '')
M=open(p+'metrics/billing-svc.csv').read().splitlines();print(M[0]);print(M[-1])