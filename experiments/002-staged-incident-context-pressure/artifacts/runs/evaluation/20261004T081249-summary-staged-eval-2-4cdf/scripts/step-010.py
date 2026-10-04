L=open('/task/fixtures/stage-3/logs/payments-api.log').readlines()
h=[i+1 for i,l in enumerate(L) if '20/20' in l]
print(len(h),h[:3])
if h:print(L[h[0]-1].strip()[:170])