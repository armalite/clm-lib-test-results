b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.strip()[:220])
L=open(b+'logs/payments-api.log').readlines()
h=[i+1 for i,l in enumerate(L) if 'pool exhausted' in l]
print(len(h),h[:5])
if h:print(L[h[0]-1].strip()[:180])